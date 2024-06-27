from flask import current_app as app
from pymongo import MongoClient

client = MongoClient(app.config['MONGO_URI'])
db = client.social_poster
tokens_collection = db.tokens
