#!/usr/bin/python
# very simple example of the use of pytest
# this script defines some tests and some test infrastructure methods used in those tests
import pytest

def func(x):
    return x + 1

@pytest.mark.test1
@pytest.mark.simple
@pytest.mark.testset1
def test_answer():
    assert func(4) == 5


