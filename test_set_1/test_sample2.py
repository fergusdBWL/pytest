#!/usr/bin/python
# very simple example of the use of pytest
# this script defines some tests and some test infrastructure methods used in those tests

def func(x):
    return x + 1

def funky(x):
    return x + 1

def test_answer():
    assert func(3) == 4

def test_answer2():
    assert funky(5) == 6
