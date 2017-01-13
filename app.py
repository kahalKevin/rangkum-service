# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals

from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words
from flask import Flask, request
import string

app = Flask(__name__)

LANGUAGE = "english"
SENTENCES_COUNT = 10

@app.route("/rangkum318149659:AAHaM5VuYYoMgjQM7rCDD8L42JbxK254b6o", methods=['POST'])
def rangkum():
    # url = "http://www.theverge.com/2016/10/18/13304090/google-pixel-phone-review-pixel-xl"	
    url = request.json['url']
    parser = HtmlParser.from_url(url, Tokenizer(LANGUAGE))
    # or for plain text files
    # parser = PlaintextParser.from_file("document.txt", Tokenizer(LANGUAGE))
    stemmer = Stemmer(LANGUAGE)
    summary = ""
    summarizer = Summarizer(stemmer)
    summarizer.stop_words = get_stop_words(LANGUAGE)
    for sentence in summarizer(parser.document, SENTENCES_COUNT):
    	temp = str(sentence)
    	temp = temp.decode('utf-8')
        summary= summary + temp + '\n'
    return summary

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()