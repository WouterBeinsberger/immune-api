from flask import request, abort
# from app.config import valid_token
import secrets
import os

from dotenv import load_dotenv, find_dotenv

# Load variables from .env file
load_dotenv(find_dotenv())

# Function to validate the bearer token
def validate_token(token):
    valid_token = os.getenv("TOKEN")

    # If a token is generated, compare with the provided token
    if valid_token:
        return token == valid_token
    
    return False

# Function to authorize the request based on the bearer token
def authorize():
    bearer_token = request.headers.get('Authorization')
    # print(bearer_token)

    if not bearer_token or not validate_token(bearer_token):
        abort(401, description='Unauthorized')

# Function to generate a token
def generate_token():
    token = secrets.token_urlsafe(32)
    
    # Set the token in the environment
    os.environ["TOKEN"] = token

    return token