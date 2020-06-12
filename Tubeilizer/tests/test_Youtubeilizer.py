
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



@pytest.fixture
def youb():
    return YBlizer()

