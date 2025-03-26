#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import json


def is_valid_password(password):
   pass

if __name__ == '__main__':
   with open("../password/password_1.json", "r", encoding="utf-8") as f:
      passwordDICT = json.load(f)
      print(passwordDICT)
      print(type(passwordDICT))