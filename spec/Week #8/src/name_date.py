#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import json


def check_date(filePATH):
    resultDICT = {
        "dates": [],
        "not_dates": []
                  }
    
    with open(filePATH, "r", encoding="utf-8") as f:
        inputLIST = json.load(f)
        print(inputLIST)
        
    
    return resultDICT


if __name__ == '__main__':
    filePATH = ""
    resultDICT = check_date(filePATH)
    print(resultDICT)