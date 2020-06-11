apikey = 'AIzaSyADadl9r_gdIqUVUD3T8OYZBJTqU66sjaE'
cid = 'UC-lHJZR3Gqxm24_Vd_AJ5Yw'

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


def get_playlist_duration():
    pl_request = youtube.playlists().list(part='contentDetails, snippet', channelId=cid)
    pl_response = pl_request.execute()
    print(pl_response)

get_playlist_duration()