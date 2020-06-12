import re
from datetime import timedelta

apikey = 'AIzaSyADadl9r_gdIqUVUD3T8OYZBJTqU66sjaE'
cid = 'UC-lHJZR3Gqxm24_Vd_AJ5Yw'
pid = 'PLYH8WvNV1YElE78ql2vvcOURM1tve_njn'

from googleapiclient.discovery import build
youtube = build('youtube', 'v3', developerKey=apikey)

def general_channel_info(user):
    """ a function that asks youtube's API information about statistics of a youtube username
    PARAMETERS:
    user = Youtube Username
    """
    request = youtube.channels().list(part='statistics',forUsername=user)
    reponse = request.execute()
    scope = 'https://www.googleapis.com/auth/youtube.force-ssl'

    #subscribers
    for subscribers in reponse['items'] :
        subs = subscribers['statistics']['subscriberCount']
        
    #views
    for views in reponse['items']:
        view = views['statistics']['viewCount']

    #videos
    for nvideos in reponse['items']:
        videos = nvideos['statistics']['videoCount']

    return f"""
    Number of Videos: {videos}
    {'-' * 20}
    Subscribers: {subs}
    {'-' * 20}
    views : {view}
"""

def channel_latest_videos(ChannelId, nvideos):
    """ a function that retrived latest uploaded video titles from a youtube channel
    PARAMETERS:
    ChannelId = Youtube Channel ID (NOT USERNAME)
    nvideos = The amount of videos you want to retrive
    """
    request = youtube.activities().list(part="snippet" ,channelId=ChannelId, maxResults=nvideos)
    response = request.execute()
    data = response['items']
    for items in data:
        print(items['snippet']['title'])


def get_playlist_duration(playlistID):
    next_page_token = None
    hours_pattern = re.compile(r'(\d+)H')
    minutes_pattern = re.compile(r'(\d+)M')
    seconds_pattern = re.compile(r'(\d+)S')
    total_seconds = 0
    while True:
        pl_request = youtube.playlistItems().list(part='contentDetails', playlistId=playlistID, maxResults=50, pageToken=next_page_token)
        pl_response = pl_request.execute()
        vid_ids = []
        for item in pl_response['items']:
            vid_ids.append(item['contentDetails']['videoId'])  


        vid_request = youtube.videos().list(part="ContentDetails", id=','.join(vid_ids))
        vid_response = vid_request.execute()
        for item in vid_response['items']:
            duration = item['contentDetails']['duration']

            hours = hours_pattern.search(duration)
            minutes = minutes_pattern.search(duration)
            seconds = seconds_pattern.search(duration)

            hours = int(hours.group(1)) if hours else 0
            minutes = int(minutes.group(1)) if minutes else 0   
            seconds = int(seconds.group(1)) if seconds else 0

            video_seconds = timedelta(hours = hours, minutes = minutes, seconds = seconds).total_seconds()

            total_seconds += video_seconds

        next_page_token = pl_response.get('nextPageToken')
        if not next_page_token:
            break

    total_seconds = int(total_seconds)

    minutes, seconds = divmod(total_seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return f"The playlist duration is {hours} hours {minutes} minutes and {seconds} seconds"

print(get_playlist_duration('PLYH8WvNV1YElE78ql2vvcOURM1tve_njn'))