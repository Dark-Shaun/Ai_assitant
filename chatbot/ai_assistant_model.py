import torch
from transformers import BlenderbotTokenizer, BlenderbotForConditionalGeneration
from typing import List, Dict
import logging
import os
from dotenv import load_dotenv

load_dotenv()

logger = logging.getLogger(__name__)

class AIAssistant:
    def __init__(self):
        model_name = "facebook/blenderbot-400M-distill"
        self.tokenizer = BlenderbotTokenizer.from_pretrained(model_name)
        self.model = BlenderbotForConditionalGeneration.from_pretrained(model_name)
        self.model.eval()
        self.conversation_history: List[Dict[str, str]] = []

    def generate_response(self, user_input: str) -> str:
        logger.info(f"Generating response for: {user_input}")

        self.conversation_history.append({"role": "user", "content": user_input})
        
        input_ids = self.tokenizer.encode(user_input, return_tensors="pt")
        
        try:
            with torch.no_grad():
                output = self.model.generate(
                    input_ids,
                    max_length=100,
                    num_return_sequences=1,
                    no_repeat_ngram_size=2,
                    top_k=50,
                    top_p=0.95,
                    temperature=0.7
                )
            
            assistant_response = self.tokenizer.decode(output[0], skip_special_tokens=True)
            
            logger.info(f"Generated response: {assistant_response}")
        except Exception as e:
            logger.error(f"Error in generate_response: {str(e)}")
            assistant_response = "I apologize, but I'm having trouble generating a response right now. Could you please try again?"

        self.conversation_history.append({"role": "assistant", "content": assistant_response})
        return assistant_response

ai_assistant = AIAssistant()