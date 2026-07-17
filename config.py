"""
Configuration module for loading API keys from environment variables.
Make sure to add this file to .gitignore!
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# API Keys
API_KEY = os.getenv('API_KEY')
API_SECRET = os.getenv('API_SECRET')
DATABASE_URL = os.getenv('DATABASE_URL')

# Add validation
if not API_KEY:
    raise ValueError("API_KEY not found. Please add it to your .env file")

# Example of how to use in your code:
# from config import API_KEY
# my_client = SomeAPIClient(api_key=API_KEY)
