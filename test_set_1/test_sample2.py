#!/usr/bin/python
# very simple example of the use of pytest
# this script defines some tests and some test infrastructure methods used in those tests
import pytest

def func(x):
    return x + 1

def funky(x):
    return x + 1

@pytest.mark.test2
@pytest.mark.simple2
@pytest.mark.testset1
def test_answer():
    assert func(3) == 4

@pytest.mark.test3
@pytest.mark.simple2
@pytest.mark.testset1
def test_answer2():
    assert funky(5) == 6
