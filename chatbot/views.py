from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
import json
import logging

logger = logging.getLogger(__name__)

try:
    from .ai_assistant_model import ai_assistant
except ImportError as e:
    logger.error(f"Failed to import AI assistant: {str(e)}")
    ai_assistant = None

def chat_view(request):
    return render(request, 'chatbot/chat.html')

@csrf_exempt
def chat_api(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user_message = data.get('message', '')
            
            logger.info(f"Received message: {user_message}")
            
            if ai_assistant is None:
                return JsonResponse({'error': 'AI assistant is not available'}, status=500)
            
            assistant_response = ai_assistant.generate_response(user_message)
            
            logger.info(f"Generated response: {assistant_response}")
            
            return JsonResponse({'response': assistant_response})
        except json.JSONDecodeError:
            logger.error("Invalid JSON received")
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        except Exception as e:
            logger.error(f"Error in chat_api: {str(e)}", exc_info=True)
            return JsonResponse({'error': str(e)}, status=500)
    logger.warning("Invalid request method")
    return JsonResponse({'error': 'Invalid request method'}, status=405)