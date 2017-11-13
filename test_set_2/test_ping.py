#!/usr/bin/python

import os

def performPing(hostname):
    response = os.system("ping -c 1 " + hostname)
    if(response==0):
        return 1
    else:
        return 0

def test_checkPing_yahoo_com():
    assert(performPing("yahoo.com") == 1)

def test_checkPing_cnn_com():
    assert(performPing("cnn.com") == 1)

