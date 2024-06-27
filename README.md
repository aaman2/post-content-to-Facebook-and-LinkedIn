# Social Poster

A web application to post content to Facebook and LinkedIn simultaneously.

## Setup

1. Create a virtual environment and install dependencies:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

2. Set up environment variables for configuration (or update `config.py` directly):
    ```bash
    export SECRET_KEY='your_secret_key'
    export MONGO_URI='your_mongodb_atlas_connection_string'
    export FACEBOOK_CLIENT_ID='your_facebook_client_id'
    export FACEBOOK_CLIENT_SECRET='your_facebook_client_secret'
    export LINKEDIN_CLIENT_ID='your_linkedin_client_id'
    export LINKEDIN_CLIENT_SECRET='your_linkedin_client_secret'
    ```

3. Run the application:
    ```bash
    python run.py
    ```

## Usage

- Link your Facebook and LinkedIn accounts.
- Share posts to both platforms simultaneously.
