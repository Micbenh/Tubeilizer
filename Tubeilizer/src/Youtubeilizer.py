import json
from googleapiclient.discovery import build

apikey = ''
youtube = build('youtube','v3', apikey)

class YBlizer():
    @staticmethod
    def display_menu():
        return """Welcome to YOUTUBELIZER
======================="""
       


a = YBlizer()
print(a.display_menu())