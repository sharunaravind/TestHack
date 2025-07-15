from dotenv import load_dotenv
import os

load_dotenv()  # 🔑 Loads from .env

USE_CLOUD = True
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
