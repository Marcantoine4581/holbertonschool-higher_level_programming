#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        tuple_r = (0, None)
    else:
        tuple_r = (len(sentence), sentence[0])
    return(tuple_r)
