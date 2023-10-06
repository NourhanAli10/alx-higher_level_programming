#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        length = len(sentence)
        first_char = "None"
    else:
        length = len(sentence)
        first_char = sentence[0]
    return (length, first_char)
