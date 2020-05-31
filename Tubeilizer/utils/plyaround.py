apikey = 'AIzaSyDdRnkdRRJOXD5K13MxsmtrJMAmLqu045g'

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


#stub for playing around
request = youtube.subscriptions().list(part='subscriberSnippet',channelId='UC-lHJZR3Gqxm24_Vd_AJ5Yw')
#response = request.execute()
#print(response)

#download captions
request = youtube.captions().list(part='snippet' ,videoId='429WCrxZqe0')
#response = request.execute()
#print(response)



#latest videos
request = youtube.activities().list(part="snippet" ,channelId="UC-lHJZR3Gqxm24_Vd_AJ5Yw", maxResults=4)
#response = request.execute()
#print(response)
'''
data = response['items']
for items in data:
    print(items['snippet']['title'])'''

#channel_latest_videos('UC-lHJZR3Gqxm24_Vd_AJ5Yw', 4)