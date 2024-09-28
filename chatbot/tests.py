from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Conversation
from .llama_model import LlamaModel
import json

class ChatbotTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.chat_url = reverse('chat')
        self.api_url = reverse('chat_api')
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.llama_model = LlamaModel()

    def test_chat_view(self):
        response = self.client.get(self.chat_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'chat.html')

    def test_chat_api(self):
        data = {'message': 'How can I lose weight?'}
        response = self.client.post(self.api_url, data=json.dumps(data), 
                                    content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn('response', response.json())

    def test_llama_model_response(self):
        user_input = "What's a good workout routine for beginners?"
        response = self.llama_model.generate_response(user_input)
        self.assertIsInstance(response, str)
        self.assertTrue(len(response) > 0)

    def test_conversation_model(self):
        conversation = Conversation.objects.create(
            user=self.user,
            user_message="How many calories should I eat?",
            bot_response="The number of calories you should eat depends on various factors..."
        )
        self.assertEqual(Conversation.objects.count(), 1)
        self.assertEqual(conversation.user, self.user)
        self.assertTrue(len(conversation.bot_response) > 0)

    def test_api_invalid_request(self):
        response = self.client.get(self.api_url)
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.json())

    def test_api_empty_message(self):
        data = {'message': ''}
        response = self.client.post(self.api_url, data=json.dumps(data), 
                                    content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.json())

    def test_conversation_creation_via_api(self):
        self.client.force_login(self.user)
        data = {'message': 'How can I build muscle?'}
        initial_count = Conversation.objects.count()
        response = self.client.post(self.api_url, data=json.dumps(data), 
                                    content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Conversation.objects.count(), initial_count + 1)

    def test_long_message_handling(self):
        long_message = "a" * 1000