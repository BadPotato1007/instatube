import os
import google.auth
import google.auth.transport.requests
import google.oauth2.credentials
import google_auth_oauthlib.flow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

# Set your API credentials JSON file path
CLIENT_SECRETS_FILE = 'creds1.json'

# Define the OAuth 2.0 scope and credentials
SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]
API_SERVICE_NAME = "youtube"
API_VERSION = "v3"

def get_authenticated_service():
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
    credentials = flow.run_local_server(port=0)

    return build(API_SERVICE_NAME, API_VERSION, credentials=credentials)

def upload_video(youtube, video_file, title, description, category_id=22, privacy_status="public"):
    request_body = {
        "snippet": {
            "title": title,
            "description": description,
            "categoryId": category_id
        },
        "status": {
            "privacyStatus": privacy_status
        }
    }

    media = MediaFileUpload(video_file, chunksize=-1, resumable=True)

    insert_request = youtube.videos().insert(
        part="snippet,status",
        body=request_body,
        media_body=media
    )

    response = None
    try:
        response = insert_request.execute()
        video_id = response.get('id', 'Unknown')
        print(f"Video id '{video_id}' was successfully uploaded.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        if response is not None:
            print(f"Response received: {response}")

if __name__ == "__main__":
    video_file_path = './final.mp4'
    video_title = 'random memes I found on the internet'
    video_description = 'cool # shorts # memes'

    youtube = get_authenticated_service()
    upload_video(youtube, video_file_path, video_title, video_description)
