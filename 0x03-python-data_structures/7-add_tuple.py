#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    new_tupule = ()
    tupule_1 = tupule_a + (0, 0)
    tupule_2 = tupule_b + (0, 0)
    new_tupule = tupule_1[0] + tupule_2[0], tupule_1[1] + tupule_2[1]
    return new_tupule
