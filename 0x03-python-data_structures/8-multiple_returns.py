#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        first = None
    else:
        first = sentence[0]
    tpl = (len(sentence), first)
    return tpl
