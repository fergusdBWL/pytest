#!/usr/bin/python
# python script which allows pytest to be run from the command line
# simply adds current working directory to the python path to allow
# packages to be found

import os
import sys

sys.path.append('.')

os.system('pytest')

