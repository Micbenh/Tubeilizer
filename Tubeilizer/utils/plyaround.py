apikey = 'AIzaSyDdRnkdRRJOXD5K13MxsmtrJMAmLqu045g'

from googleapiclient.discovery import build
youtube = build('youtube', 'v3', developerKey=apikey)


request = youtube.channels().list(part='statistics',forUsername='pewdiepie')
reponse = request.execute()

print(reponse)
print()

def general_channel_info():
    for x in reponse['items']:
        a = x['statistics']['viewCount']

    print("views:", a)

general_channel_info()