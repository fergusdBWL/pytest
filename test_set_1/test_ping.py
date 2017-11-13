#!/usr/bin/python
# do some network pinging using the PingUtils package
# this package is part of the test infrastructure defined here

from utils import PingUtils

pingUtils = PingUtils()

def test_checkPing_google_com():
    assert(pingUtils.singlePing("google.com") == 1)

def test_checkPing_xgoogle_com():
    assert(pingUtils.singlePing("xgoogle.com") == 0)

def test_checkPing_bbc_com():
    assert(pingUtils.singlePing("bbc.com") == 1)

