#!/usr/bin/python
import sys, os
import pytest
#myPath = os.path.dirname(os.path.abspath(__file__))
#sys.path.insert(0, myPath + '/../utils/')

# do some network pinging using the PingUtils package
# this package is part of the test infrastructure defined here

from utils import PingUtils

pingUtils = PingUtils()

@pytest.mark.test4
@pytest.mark.ping
@pytest.mark.testset1
def test_checkPing_google_com():
  assert(pingUtils.singlePing("google.com") == 1)

@pytest.mark.test5
@pytest.mark.ping
@pytest.mark.testset1
@pytest.mark.xfail
def test_checkPing_xgoogle_com():
  assert(pingUtils.singlePing("xgoogle.com") == 0)

@pytest.mark.test6
@pytest.mark.ping
@pytest.mark.testset1
def test_checkPing_bbc_com():
  assert(pingUtils.singlePing("bbc.com") == 1)
 
