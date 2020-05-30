

from utils.plyaround import *

apikey = 'AIzaSyDdRnkdRRJOXD5K13MxsmtrJMAmLqu045g'
from googleapiclient.discovery import build
youtube = build('youtube', 'v3', developerKey=apikey)

class YBlizer():

    @staticmethod
    def display_menu():
        return """Welcome to YOUTUBELIZER
======================="""
       
    def genChannelInfo(self):
        user = input("Enter Youtube Channel Username: ")
        request = youtube.channels().list(
            part='statistics',
            forUsername=user
        )
        response = request.execute()



a = YBlizer()
print(a.genChannelInfo())