import json
from googleapiclient.discovery import build

apikey = 'AIzaSyDdRnkdRRJOXD5K13MxsmtrJMAmLqu045g'
youtube = build('youtube','v3', developerKey=apikey)

class YBlizer():
    @staticmethod
    def display_menu():
        return """Welcome to YOUTUBELIZER
======================="""
       


a = YBlizer()
#print(a.channel_overview())

