from utilities.json_operations import process_and_append_to_json
from tqdm import tqdm
from googleapiclient.errors import HttpError
from youtubesearchpython import Playlist, playlist_from_channel_id

## Get all info for a video by video_id
def get_video_detail(youtube, video_id):
    try:
        request = youtube.videos().list(
            part="snippet,contentDetails",
            maxResults=50,
            id=video_id
        )
        response = request.execute()
        return response
    except HttpError as e:
        print('Error response status code : {0}, reason : {1}'.format(e.resp.status, e.error_details))
        return None

## Get all videos in all playlist
def get_all_videos_in_all_playlist(youtube, channel_id):
    try:
        playlists_request = youtube.playlists().list(
            part="snippet",
            channelId=channel_id,
            maxResults=50  # You can adjust this to get more or fewer playlists per request
        )
        playlists_response = playlists_request.execute()

        all_videos = []

        for playlist_item in playlists_response.get("items", []):
            playlist_id = playlist_item["id"]
            playlist_title = playlist_item["snippet"]["title"]

            # Fetch videos for the current playlist
            videos_request = youtube.playlistItems().list(
                part="snippet",
                playlistId=playlist_id,
                maxResults=50  # You can adjust this to get more or fewer videos per request
            )
            videos_response = videos_request.execute()

            # Append the videos and playlist information to the result list
            all_videos.extend([(video["snippet"], playlist_title) for video in videos_response.get("items", [])])

        return all_videos
    except HttpError as e:
        print('Error response status code : {0}, reason : {1}'.format(e.resp.status, e.error_details))
        return None

# Scrape video info
def Scrape_video_info(channel_info, num_video=100):
    for channel_id, row in tqdm(channel_info.items(), desc="Processing Channels"):
        data_dict = {}

        # Retrieve all videos
        try:
            playlist = Playlist(playlist_from_channel_id(channel_id))
            if num_video == 100:
                all_videos = playlist.videos
            else:
                all_videos = []
                iter_time = (num_video + 100 - 1) // 100 
                while playlist.hasMoreVideos and (iter_time > 0):
                    all_videos += playlist.videos
                    playlist.getNextVideos()
                    iter_time -= 1
        except:
            print(f"\n Channel: {row['channel_title']} is skipped!")
            continue

        # Preprocess videos to extract required information
        video_info = [{
            'video_title': video['title'],
            'video_id': video['id']
        } for video in all_videos]

        data_dict[channel_id] = {
            'channel_title': row['channel_title'],
            'channel_link': row['channel_link'],
            'video': {
                'video_title': [video['video_title'] for video in video_info],
                'video_id': [video['video_id'] for video in video_info]
            }
        }
        # Call the nested function to process and append data to the JSON file
        process_and_append_to_json(data_dict, './data/channel_video_info.json')