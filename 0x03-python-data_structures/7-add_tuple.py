#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_b) < 2 or len(tuple_b) == 0:
        for i in range(len(tuple_b), 2):
            tuple_b += (0,)
    elif len(tuple_b) > 2:
        tuple_b = (tuple_b[0], tuple_b[1])
    if len(tuple_a) < 2 or len(tuple_a) == 0:
        for i in range(len(tuple_a), 2):
            tuple_a += (0,)
    elif len(tuple_a) > 2:
        tuple_a = (tuple_a[0], tuple_a[1])
    new_tuple = ()
    for a, b in zip(tuple_a, tuple_b):
        c = a + b
        new_tuple += (c,)
    return new_tuple
