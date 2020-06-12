
import os 
import sys
sys.path.append(os.getcwd())

from utils.plyaround import general_channel_info, get_playlist_duration
apikey = 'AIzaSyADadl9r_gdIqUVUD3T8OYZBJTqU66sjaE'
from googleapiclient.discovery import build
youtube = build('youtube', 'v3', developerKey=apikey)

class YBlizer():
    @staticmethod
    def display_menu():
        return """Welcome to YOUTUBELIZER
======================="""
       
    def genChannelInfo(self):
        user = input("Enter Youtube Channel Username: ")
        return general_channel_info(user)

    def Playlist_duration(self):
        playlistID = input("Please enter the wanted playlist ID: ")
        return get_playlist_duration(playlistID)




a = YBlizer()
print(a.Playlist_duration())

