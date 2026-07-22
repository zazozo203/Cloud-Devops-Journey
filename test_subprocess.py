#!/usr/bin/env python3
import os 
import subprocess
cmd = 'cat commands.py'
rs = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
rs.wait()
sr= rs.communicate()
out,err= sr 


print(out)
print(err)


