
import os 
import sys

from googleapiclient.discovery import build
sys.path.append(os.getcwd())
print(sys.path)
from utils.plyaround import general_channel_info, channel_latest_videos


class YBlizer():
    def __init__(self, apikey):
        self.apikey = apikey
        youtube = build('youtube', 'v3', developerKey=apikey)

    @staticmethod
    def display_menu():
        return """Welcome to YOUTUBELIZER
======================="""
       
    def genChannelInfo(self):
        user = input("Enter Youtube Channel Username: ")
        return general_channel_info(user)

    def genLatestVideos(self):
        channelID = input("Enter Youtube Channel Username: ")
        try:
            nvideos = int(input("How many videos do you want to pull? "))
        except Exception:
            ("We only accept a number")
        return channel_latest_videos(channelID, nvideos)




a = YBlizer('AIzaSyDdRnkdRRJOXD5K13MxsmtrJMAmLqu045g')
#print(a.genChannelInfo())
a.genLatestVideos()