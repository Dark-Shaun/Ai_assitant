# fitness_bot/chatbot/huggingface_model.py

import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from typing import List, Dict
import logging
import os
from dotenv import load_dotenv

load_dotenv()

logger = logging.getLogger(__name__)

class AdvancedChatbot:
    def __init__(self):
        model_name = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=torch.float16)
        self.model.eval()
        self.conversation_history: List[Dict[str, str]] = []

    def generate_response(self, user_input: str) -> str:
        logger.info(f"Generating response for: {user_input}")

        self.conversation_history.append({"role": "user", "content": user_input})
        
        prompt = self.prepare_prompt(user_input)

        try:
            input_ids = self.tokenizer.encode(prompt, return_tensors="pt")
            
            with torch.no_grad():
                output = self.model.generate(
                    input_ids,
                    max_new_tokens=150,
                    temperature=0.7,
                    top_p=0.95,
                    do_sample=True
                )
            
            bot_response = self.tokenizer.decode(output[0], skip_special_tokens=True)
            bot_response = bot_response.split("Human:")[0].strip()
            
            logger.info(f"Generated response: {bot_response}")
        except Exception as e:
            logger.error(f"Error in generate_response: {str(e)}")
            bot_response = "I apologize, but I'm having trouble generating a response right now. Could you please try again?"

        self.conversation_history.append({"role": "assistant", "content": bot_response})
        return bot_response

    def prepare_prompt(self, user_input: str) -> str:
        prompt = "You are a helpful AI assistant capable of answering questions on various topics, providing explanations, and assisting with tasks. Respond to the user's messages in a friendly and informative manner.\n\n"
        
        for message in self.conversation_history[-5:]:
            if message["role"] == "user":
                prompt += f"Human: {message['content']}\n"
            else:
                prompt += f"Assistant: {message['content']}\n"
        
        prompt += f"Human: {user_input}\nAssistant:"
        return prompt
