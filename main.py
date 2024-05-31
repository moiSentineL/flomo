#! /bin/env python3
from datetime import datetime
start = datetime.now()
while True:
	now = datetime.now()
	print("\r"+str(now-start), end="")

#Source: https://gist.github.com/dzamlo/9debd3284750f3eed2a4654f0ec908e8
