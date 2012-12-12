import ast
import json
import time
import utils
import random
import pymongo
import networkx as nx
from collections import defaultdict
from scipy.sparse import *

class FindPath(object):
	def __init__(self):
		self.db = utils.connect_db("STOS")
		self.graph = nx.DiGraph()
		self.users = set()
	
	def load(self):
		print "Loading Data, This Can Take A Few Minutes"
		f = open("data.json")
		while 1:
			line = f.readline()
			if not line:
				break
			temp = json.loads(line)
			t = ast.literal_eval(temp.keys()[0])
			self.graph.add_edge(t[0], t[1], temp.values()[0])
		self.users = set(self.graph.nodes())
	
	def user_exists(self, user):
		if user in self.users:
			return True
		return False
	
	def path_exists(self, start, end):
		if nx.has_path(self.graph, start, end):
			return True
		return False
	
	def get_path(self, start, end):
		return nx.shortest_path(self.graph, start, end)
	
	def get_tweet(self, user, subject):
		user_tweets = self.db.tweets.find({"screen_name":user[1:]})
		for tweet in user_tweets:
			if subject in tweet["text"]:
				return user + ": " + tweet["text"]
		user_tweets = self.db.tweets.find({"screen_name":subject[1:]})
		for tweet in user_tweets:
			if user in tweet["text"]:
				return subject + ": " + tweet["text"]
	
	def get_random_user(self):
		return random.choice(list(self.users))