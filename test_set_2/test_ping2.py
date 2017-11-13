#!/usr/bin/python

import os
from utils import PingUtils

pingUtils = PingUtils()

def test_checkPing_yahoo_com():
    assert(pingUtils.singlePing("yahoo.com") == 1)

def test_checkPing_cnn_com():
    assert(pingUtils.singlePing("cnn.com") == 1)

