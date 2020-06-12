
import os 
import sys
sys.path.append(os.getcwd())
import pytest
from unittest import mock
from src.Youtubeilizer import YBlizer
from io import StringIO

def test_menu_display(youb):
    assert youb.display_menu() == """Welcome to YOUTUBELIZER
======================="""

def test_playlist_duration_retrive(youb, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda s: 'PLYH8WvNV1YElE78ql2vvcOURM1tve_njn')
    i = youb.Playlist_duration()
    assert i == 'The playlist duration is 29 hours 56 minutes and 52 seconds'



@pytest.fixture
def youb():
    return YBlizer()

