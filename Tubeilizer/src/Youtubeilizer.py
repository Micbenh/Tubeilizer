
import os 
import sys
sys.path.append(os.getcwd())

from utils.plyaround import general_channel_info 
apikey = ''
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



a = YBlizer()
print(a.genChannelInfo())
