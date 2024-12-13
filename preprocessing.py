import string
import nltk
from nltk.tokenize import word_tokenize
import re

def lower(X):
    # lower cases the data
    return X.str.lower()

def punc_removal(X):
    # removes punctuation marks
    return X.str.translate(str.maketrans('', '', string.punctuation))

def spec_char_removal(X):
    # removes special characters
    return X.str.replace(r'[^a-zA-Z\s]', '', regex = True)

def tokenize(X):
    # splits input into tokens/words
    nltk.download('punkt')
    return word_tokenize(X)