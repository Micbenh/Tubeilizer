
import os 
import sys

print(os.getcwd())
sys.path.append(os.getcwd())
print(sys.path)
print
import pytest
from Yout.Youtubeilizer import YBlizer


def test_menu_display(youb):
    assert youb.display_menu() == """Welcome to YOUTUBELIZER
======================="""


@pytest.fixture
def youb():
    return YBlizer()

