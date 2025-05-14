#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import json

def word_count():
    pass

def most_common_word():
    pass

def capital_word():
    pass

if __name__ == '__main__':
    filePATH = ""
    with open(filePATH,"r",encoding="utf-8") as f:
        inputLIST=json.load(f)
    
    
# output
# Word counts per sentence: [4, 5, 6, 5, 5]
# Most common word: 'Python'
# Words starting with capital: ['I', 'Python', 'NLP', 'Natural', 'Language', 'Processing', 'Learning']
