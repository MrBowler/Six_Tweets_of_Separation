README for "Six Tweets of Separation" Crawl Code
================================================
What needs to be installed:
	* tweepy
	* ujson
	
NOTE: Be sure add Twitter user name and password in get_tweets.py

How to run:
	* Change directory to this file
	* Run this line:
		$ python get_tweets.py
	* This will run until the user presses ctrl+C
	* Tweets will be added to test.json
	* After running get_tweets.py, run this line:
		$ python clean_file.py
	* clean_file.py is used to remove junk lines
	* The final result is in tweets.json (test.json can be deleted)