#!/usr/bin/python3
import sys; 
from notebook.auth import passwd; 
print(passwd(sys.argv[1]).replace(' ', '').replace('usha', 'sha'));
