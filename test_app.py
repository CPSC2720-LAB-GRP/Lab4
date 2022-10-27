import pytest

from app import load_wiki_summary
from app import answer_question

def func(x):
    return x + 1

def test_answer():
    assert func(3) == 4
