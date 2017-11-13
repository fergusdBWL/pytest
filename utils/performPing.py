#!/usr/bin/python

import os

def performPing(hostname):
    response = os.system("ping -c 1 " + hostname)
    if(response==0):
        return 1
    else:
        return 0

