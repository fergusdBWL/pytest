#!/usr/bin/python

import os

class PingUtils:
    def singlePing(self,hostname):
        response = os.system("ping -c 1 " + hostname)
        if(response==0):
            return 1
        else:
            return 0

