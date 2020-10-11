import sys
import os
import argparse

from nltk.parse.corenlp import CoreNLPParser
from nltk.tag.stanford import StanfordPOSTagger, StanfordNERTagger
from nltk.tokenize.stanford import StanfordTokenizer
from nltk.tree import *
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer, PorterStemmer
import nltk

java_path = '/usr/bin/java'
os.environ['CLASSPATH'] = java_path

input_string = input("Input a string: ")

parser = CoreNLPParser(url='http://localhost:9000')

p = list(parser.parse(input_string.split()))


print(p)