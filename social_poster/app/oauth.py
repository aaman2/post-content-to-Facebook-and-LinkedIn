from flask import Blueprint, redirect, url_for, request, session
import requests
from .models import tokens_collection

oauth = Blueprint('oauth', __name__)

# Facebook OAuth
@oauth.route('/login/facebook')
def login_facebook():
    return redirect(f"https://www.facebook.com/v10.0/dialog/oauth?client_id={current_app.config['FACEBOOK_CLIENT_ID']}&redirect_uri={url_for('oauth.facebook_callback', _external=True)}&scope=public_profile,pages_manage_posts,pages_read_engagement")

@oauth.route('/callback/facebook')
def facebook_callback():
    code = request.args.get('code')
    response = requests.get(f"https://graph.facebook.com/v10.0/oauth/access_token?client_id={current_app.config['FACEBOOK_CLIENT_ID']}&redirect_uri={url_for('oauth.facebook_callback', _external=True)}&client_secret={current_app.config['FACEBOOK_CLIENT_SECRET']}&code={code}")
    data = response.json()
    session['facebook_token'] = data['access_token']
    tokens_collection.update_one({'platform': 'facebook'}, {'$set': {'token': data['access_token']}}, upsert=True)
    return redirect(url_for('main.home'))

# LinkedIn OAuth
@oauth.route('/login/linkedin')
def login_linkedin():
    return redirect(f"https://www.linkedin.com/oauth/v2/authorization?response_type=code&client_id={current_app.config['LINKEDIN_CLIENT_ID']}&redirect_uri={url_for('oauth.linkedin_callback', _external=True)}&scope=w_member_social")

@oauth.route('/callback/linkedin')
def linkedin_callback():
    code = request.args.get('code')
    response = requests.post('https://www.linkedin.com/oauth/v2/accessToken', data={
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': url_for('oauth.linkedin_callback', _external=True),
        'client_id': current_app.config['LINKEDIN_CLIENT_ID'],
        'client_secret': current_app.config['LINKEDIN_CLIENT_SECRET']
    })
    data = response.json()
    session['linkedin_token'] = data['access_token']
    tokens_collection.update_one({'platform': 'linkedin'}, {'$set': {'token': data['access_token']}}, upsert=True)
    return redirect(url_for('main.home'))
