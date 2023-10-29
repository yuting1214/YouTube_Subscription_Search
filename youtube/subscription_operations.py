from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

def get_subscription(youtube):
    try:
        request = youtube.subscriptions().list(
            part="snippet,contentDetails",
            maxResults=50,
            mine=True
        )
        response = request.execute()
        return response
    except HttpError as e:
        print('Error response status code : {0}, reason : {1}'.format(e.resp.status, e.error_details))
        return None

def get_all_subscriptions(youtube):
    subscriptions = []
    page_token = None

    while True:
        try:
            request = youtube.subscriptions().list(
                part="snippet,contentDetails",
                maxResults=50,
                mine=True,
                pageToken=page_token
            )
            response = request.execute()

            # Add the current batch of subscriptions to our list
            subscriptions.extend(response.get('items', []))

            # If there's no nextPageToken, we've retrieved all subscriptions
            page_token = response.get('nextPageToken')
            if not page_token:
                break

        except HttpError as e:
            print('Error response status code : {0}, reason : {1}'.format(e.resp.status, e.error_details))
            break

    return subscriptions
