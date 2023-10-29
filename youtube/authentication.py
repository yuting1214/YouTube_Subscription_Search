import os
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

SCOPES = ["https://www.googleapis.com/auth/youtube.readonly"]
CLIENT_FILE = "./API_key/youtube_credential.json"
TOKEN_FILE = "./API_key/token.json"
API_SERVICE_NAME = "youtube"
API_VERSION = "v3"

def load_credentials():
    """Load credentials from token file if it exists."""
    if os.path.exists(TOKEN_FILE):
        return Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
    return None


def save_credentials(creds):
    """Save credentials to a token file."""
    with open(TOKEN_FILE, 'w') as token:
        token.write(creds.to_json())


def refresh_credentials(creds):
    """Refresh expired credentials."""
    creds.refresh(Request())
    save_credentials(creds)


def authenticate():
    """Authenticate with OAuth2 and return the credentials."""
    flow = InstalledAppFlow.from_client_secrets_file(CLIENT_FILE, SCOPES)
    creds = flow.run_local_server(port=0)
    save_credentials(creds)
    return creds


def get_authenticated_service():
    creds = load_credentials()

    if not creds:
        creds = authenticate()
    elif creds.expired and creds.refresh_token:
        refresh_credentials(creds)

    return build(API_SERVICE_NAME, API_VERSION, credentials=creds)