#!/usr/bin/python
# python class to demonstrate the use of a package within the test framework
# in this case a class that allows things to be pinged

import os

class PingUtils:
    def singlePing(self,hostname):
        response = os.system("ping -c 1 " + hostname)
        if(response==0):
            return 1
        else:
            return 0

