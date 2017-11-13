#!/usr/bin/python

import os
from utils import performPing

#def performPing(hostname):
#    response = os.system("ping -c 1 " + hostname)
#    if(response==0):
#        return 1
#    else:
#        return 0

def test_checkPing_google_com():
    assert(performPing("google.com") == 1)

def test_checkPing_xgoogle_com():
    assert(performPing("xgoogle.com") == 0)

def test_checkPing_bbc_com():
    assert(performPing("bbc.com") == 1)

