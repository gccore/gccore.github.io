#!/usr/bin/python

import subprocess
import os
import sys
from pathlib import Path

list = os.listdir();
for name in list:
    name = str(name)
    the_name = Path(name).stem;
    print("<li>LINK(" + the_name + "," + sys.argv[1] + "/" + name + ")</li>")
