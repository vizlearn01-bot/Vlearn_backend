import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()


DEFAULT_GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-flash-latest")

class LLMClient:
    """
    Modular abstraction for the AI model.
    Connects to Gemini API for lesson generation.
    """
    @staticmethod
    def generate(prompt: str, model_name: str = DEFAULT_GEMINI_MODEL) -> str:
        api_key = os.environ.get("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY not found in environment variables. Please add it to your .env file.")
            
        genai.configure(api_key=api_key)
        
        # Configure model
        generation_config = {
            "temperature": 0.7,
            "top_p": 0.95,
            "top_k": 64,
            "max_output_tokens": 8192,
        }
        
        model = genai.GenerativeModel(
            model_name=model_name,
            generation_config=generation_config,
        )
        
        try:
            response = model.generate_content(prompt)
            return response.text
        except Exception as e:
            print(f"Error calling Gemini API: {str(e)}")
            raise e
