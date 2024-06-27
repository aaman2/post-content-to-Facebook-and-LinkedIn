import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_secret_key'
    MONGO_URI = os.environ.get('MONGO_URI') or 'your_mongodb_atlas_connection_string'
    FACEBOOK_CLIENT_ID = os.environ.get('FACEBOOK_CLIENT_ID') or 'your_facebook_client_id'
    FACEBOOK_CLIENT_SECRET = os.environ.get('FACEBOOK_CLIENT_SECRET') or 'your_facebook_client_secret'
    LINKEDIN_CLIENT_ID = os.environ.get('LINKEDIN_CLIENT_ID') or 'your_linkedin_client_id'
    LINKEDIN_CLIENT_SECRET = os.environ.get('LINKEDIN_CLIENT_SECRET') or 'your_linkedin_client_secret'
