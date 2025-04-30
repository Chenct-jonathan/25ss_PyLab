#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import re

def extract_userinfo(string):
    pat = "([\w]+)@([a-z]+).(com|net)"
    info = re.search(pat, string)
    
    
    # username --> info.group(1)
    # domain --> info.group(2)+info.group(3)
    
    
    # return [username, domain]
    pass


if __name__ == '__main__':
    with open("../data/sheet.txt", "r", encoding="utf-8") as f:
        inputLIST = f.readlines()
        print(inputLIST)
        
        
    result = []
    for string in inputLIST:
        # extract info
        extract_userinfo(string)
        