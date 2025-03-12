#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def case_extract(inputSTR):
    
    outputDICT = {
        "Subject": "",
        "Object": "",
        "Verb": "",
    }
    
    outputDICT["Subject"] = inputSTR[:inputSTR.find("は")]
    outputDICT["Object"] = inputSTR[inputSTR.find("は")+1:inputSTR.find("を")]
    outputDICT["Verb"] = inputSTR[inputSTR.find("を")+1:]
    
    return outputDICT

if __name__ == '__main__':
    x = "私はラーメンを食べます"
    y = case_extract(x)
    print(y)