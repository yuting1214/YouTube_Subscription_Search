import json
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from utilities.json_operations import process_and_append_to_json 

# Get Channel information by username
def get_channel_info(youtube, username="schafer5"):
    try:
        request = youtube.channels().list(
            part="snippet,contentDetails,statistics",
            forUsername=username
        )
        response = request.execute()
        return response
    except HttpError as e:
        print('Error response status code : {0}, reason : {1}'.format(e.resp.status, e.error_details))
        return None

# Get Channel information by channel_id
def get_channel_info_by_id(youtube, id):
    try:
        request = youtube.channels().list(
            part="snippet,contentDetails,statistics",
            id=id
        )
        response = request.execute()
        return response
    except HttpError as e:
        print('Error response status code : {0}, reason : {1}'.format(e.resp.status, e.error_details))
        return None

# Create a json file including all info for subscribed channels
def create_channel_info_json(subscription_list):
    output = {}
    for channel in subscription_list:
        channel_id = channel['snippet']['resourceId']['channelId']
        channel_title = channel['snippet']['title']
        channel_link = "https://www.youtube.com/channel/" + channel_id
        channel_thumbnail = channel['snippet']['thumbnails']['medium']['url']
        channel_description = channel['snippet']['description']
        output[channel_id] = {
            'channel_title': channel_title,
            'channel_link': channel_link,
            'channel_thumbnail': channel_thumbnail,
            'channel_description': channel_description
        }
    file_path = './data/channel_info.json'
    with open(file_path, 'w') as file:
        json.dump(output, file, indent=4)
    return None

# Update the json file including all info for subscribed channels
def update_channel_info_json(subscription_list):
    # Prepare channel info data from subscription list
    output = {}
    for channel in subscription_list:
        channel_id = channel['snippet']['resourceId']['channelId']
        channel_title = channel['snippet']['title']
        channel_link = "https://www.youtube.com/channel/" + channel_id
        channel_thumbnail = channel['snippet']['thumbnails']['medium']['url']
        channel_description = channel['snippet']['description']
        output[channel_id] = {
            'channel_title': channel_title,
            'channel_link': channel_link,
            'channel_thumbnail': channel_thumbnail,
            'channel_description': channel_description
        }

    # Append or merge the new data to the existing JSON
    file_path = './data/channel_info.json'
    process_and_append_to_json(output, file_path)
    return None
