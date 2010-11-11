# -*- coding: utf-8 -*-

def parsenumber(text):
        if not all(x in "0123456789," for x in text):
            return
        text = (text + "00").split(",")
        if len(text) > 2:
            return
        return int("".join(text[0:1]) + "".join(text[1:2])[0:2])
