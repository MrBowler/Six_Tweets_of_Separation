#!/usr/bin/env python
import tweepy
import json
import sys
from textwrap import TextWrapper

f = open('test.json','w')

class StreamWatcherListener(tweepy.StreamListener):
    status_wrapper = TextWrapper(width=60, initial_indent='    ', subsequent_indent='    ')
    def on_status(self, status):
        try:
            f.write("\n")
            f.write("{\"screen_name\":")
            f.write(json.dumps(status.author.screen_name))
            f.write(", \"user_id\":")
            f.write(json.dumps(status.user.id))
            f.write(", \"text\":\"")
            f.write(status.text)
            f.write("\", \"tweet_id\":")
            f.write(json.dumps(status.id))
            f.write("}")
            f.write("\n")
        except:
            # Catch any unicode errors while printing to console
            # and just ignore them to avoid breaking application.
            pass
    def on_error(self, status_code):
        print 'An error has occured! Status code = %s' % status_code
        return True  # keep stream alive
    def on_timeout(self):
        f.close()
        print 'Snoozing Zzzzzz'

# Change USER_NAME and PASSWORD to Twitter info
auth = tweepy.BasicAuthHandler(USER_NAME, PASSWORD)
stream = tweepy.Stream(auth, StreamWatcherListener(), timeout=60)
stream.sample()
f.close()
