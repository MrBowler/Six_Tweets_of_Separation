import ast
import json
import time
import utils
import random
import pymongo
import networkx as nx
from collections import defaultdict
from scipy.sparse import *

def main():
	print "Loading Data, This Can Take A Few Minutes"
	db = utils.connect_db("STOS")
	graph = nx.DiGraph()
	f = open("data.json")
	users = set()
	while 1:
		line = f.readline()
		if not line:
			break
		temp = json.loads(line)
		t = ast.literal_eval(temp.keys()[0])
		graph.add_edge(t[0], t[1], temp.values()[0])
		users.add(t[0])
		users.add(t[1])
		if len(users) > 3400000:
			break
	users = set(graph.nodes())
	quit_loop = False
	while not quit_loop:
		start = ""
		end = ""
		print ""
		print "For random node, enter \"random\". To quit, enter \"quit\"."
		var = raw_input("Enter Start Node: ")
		if var == "quit":
			quit_loop = True
			continue
		if var == "random" or var == "":
			start = random.choice(graph.nodes())
		else:
			if var[0] != "@":
				var = "@" + var
			if var not in users:
				print "User not found. Try again."
				continue
			start = var
		got_end = False
		while not got_end:
			var = raw_input("Enter End Node: ")
			if var == "random" or var == "":
				end = random.choice(graph.nodes())
			else:
				if var[0] != "@":
					var = "@" + var
				if var not in users:
					print "User not found. Try again."
					continue
				end = var
			got_end = True
		if nx.has_path(graph, start, end):
			print "Finding path. Please wait."
			path = nx.astar_path(graph, start, end)
			print ""
			print "The path between " + start + " and " + end + " is:"
			prev_tweet = ""
			print path
			print ""
			for user in path:
				if user == end:
					continue
				got_tweet = False
				user_tweets = db.tweets.find({"screen_name":user[1:]})
				for tweet in user_tweets:
					if path[path.index(user) + 1] in tweet["text"]:
						if prev_tweet == tweet["text"]:
							continue
						else:
							print user + ":"
							print tweet["text"]
							prev_tweet = tweet["text"]
							print ""
							got_tweet = True
							break
				if not got_tweet:
					user_tweets = db.tweets.find({"screen_name":path[path.index(user) + 1][1:]})
					for tweet in user_tweets:
						if user in tweet["text"]:
							if prev_tweet == tweet["text"]:
								continue
							else:
								print path[path.index(user) + 1] + ":"
								print tweet["text"]
								prev_tweet = tweet["text"]
								print ""
								break
		else:
			print "Sorry, there is no path between " + start + " and " + end + "."
	print "Now Quiting"

if __name__ == "__main__":
	main()
