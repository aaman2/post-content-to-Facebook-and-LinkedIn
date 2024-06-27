from flask import Blueprint, render_template, session, request, redirect, url_for
import requests
from .models import tokens_collection

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('home.html')

@main.route('/share', methods=['POST'])
def share():
    content = request.form['content']
    
    # Post to Facebook
    fb_token = tokens_collection.find_one({'platform': 'facebook'})['token']
    fb_response = requests.post(f"https://graph.facebook.com/me/feed?message={content}&access_token={fb_token}")
    
    # Post to LinkedIn
    linkedin_token = tokens_collection.find_one({'platform': 'linkedin'})['token']
    linkedin_response = requests.post('https://api.linkedin.com/v2/ugcPosts', headers={
        'Authorization': f'Bearer {linkedin_token}',
        'Content-Type': 'application/json'
    }, json={
        "author": "urn:li:person:your_linkedin_user_id",
        "lifecycleState": "PUBLISHED",
        "specificContent": {
            "com.linkedin.ugc.ShareContent": {
                "shareCommentary": {
                    "text": content
                },
                "shareMediaCategory": "NONE"
            }
        },
        "visibility": {
            "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
        }
    })
    
    if fb_response.status_code == 200 and linkedin_response.status_code == 201:
        return "Posted successfully!"
    else:
        return "Error posting to Facebook or LinkedIn", 500
