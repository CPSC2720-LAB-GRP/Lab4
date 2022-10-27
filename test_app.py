import pytest
import wikipedia
import streamlit as st
from tokenizers import Tokenizer
from transformers import pipeline, Pipeline 

from app import load_wiki_summary
from app import answer_question

def test_load_wiki_summary_query(x):
    testResults = wikipedia.search("Calgary")
    testSummary = wikipedia.summary(results[0], sentences=10)
    return testSummary
    
def test_load_wiki_summary():   
     results = wikipedia.search("Calgary")
     summary = wikipedia.summary(results[0], sentences=10)    
    
     assert test_load_wiki_summary_query(x)=summary
    
def func(x):
    return x + 1
    
def test_answer():
    assert func(3) == 4
