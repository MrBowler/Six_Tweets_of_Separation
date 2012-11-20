#!/usr/bin/env python

f = open("test.json")
g = open("tweets.json", "a")

while 1:
	line = f.readline()
	if not line:
		break
	if len(line) > 1 and line[-2] == '}' and line[0:15] == "{\"screen_name\":" and '@' in line:
		g.write(line)
