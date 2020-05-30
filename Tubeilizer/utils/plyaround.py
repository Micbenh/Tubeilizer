apikey = ''

from googleapiclient.discovery import build
youtube = build('youtube', 'v3', developerKey=apikey)

def general_channel_info(user):
    """ a function that asks youtube's API information about statistics of a youtube username
    PARAMETERS:
    user = Youtube Username
    """
    request = youtube.channels().list(part='statistics',forUsername=user)
    reponse = request.execute()

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

#stub for playing around
request = youtube.channels().list(part='statistics',forUsername='pewdiepie')
reponse = request.execute()
print(reponse)