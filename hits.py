import re
import math
import time
import utils
import scipy as sp
import numpy as np
from collections import defaultdict
from scipy.sparse import *

class HITS(object):
	def __init__(self):
		self.user_connections = defaultdict(set)
		self.user_to_id = defaultdict(int)
		self.id_to_user = defaultdict(str)
		self.auth = 0
		self.hub = 0
	
	def set_users(self, tweets):
		count = 0
		for tweet in tweets:
			if "@" + tweet["screen_name"] not in self.user_to_id:
				self.user_to_id["@" + tweet["screen_name"]] = count
				self.id_to_user[count] = "@" + tweet["screen_name"]
				count += 1
			splitter = re.compile(r'(\s+|\S+)')
			tokens = splitter.findall(tweet["text"])
			for token in tokens:
				if "@" in token:
					x = 0
					while token[x] != "@":
						x += 1
					token = token[x:]
					if re.match("[\w\d_-]*$", token[1:]):
						if token not in self.user_to_id:
							self.user_to_id[token] = count
							self.id_to_user[count] = token
							count += 1
						key = "@" + tweet["screen_name"]
						self.user_connections[key].add(token)
					else:
						if token[:-1] not in self.user_to_id:
							self.user_to_id[token[:-1]] = count
							self.id_to_user[count] = token[:-1]
							count += 1
						key = "@" + tweet["screen_name"]
						self.user_connections[key].add(token[:-1])

	def set_A(self):
		A = lil_matrix((len(self.user_to_id.keys()),len(self.user_to_id.keys())))
		for user in self.user_connections:
			for mention in self.user_connections[user]:
				A[self.user_to_id[user],self.user_to_id[mention]] = 1
		return csr_matrix(A)
	
	def hubs_and_authorities(self, tweets):
		self.set_users(tweets)
		A = self.set_A()
		AT = csr_matrix.transpose(A)
		self.auth = csr_matrix(np.ones((len(self.user_to_id.keys()),1)))
		self.hub = csr_matrix(np.ones((len(self.user_to_id.keys()),1)))
		test_auth = csr_matrix(np.zeros((len(self.user_to_id.keys()),1)))
		test_hub = csr_matrix(np.zeros((len(self.user_to_id.keys()),1)))
		
		while not np.array_equal(np.asarray(self.auth.todense()),np.asarray(test_auth.todense())) or not np.array_equal(np.asarray(self.hub.todense()),np.asarray(test_hub.todense())):
			test_auth = self.auth.copy()
			test_hub = self.hub.copy()
			self.auth = AT.dot(self.hub)
			norm = sp.sqrt(sp.sum(sp.absolute(np.asarray(self.auth.todense()))**2))
			self.auth = csr_matrix(np.asarray(self.auth.todense()) / norm)
			self.hub = A.dot(self.auth)
			norm = sp.sqrt(sp.sum(sp.absolute(np.asarray(self.hub.todense()))**2))
			self.hub = csr_matrix(np.asarray(self.hub.todense()) / norm)
	
	def get_matrix(self, tweets):
		self.set_users(tweets)
		return self.set_A()
	
	def get_hub(self, tweets):
		self.hubs_and_authorities(tweets)
		temp = csr_matrix.transpose(self.hub)
		return np.asarray(temp.todense()).tolist()[0]
		
	def get_auth(self, tweets):
		self.hubs_and_authorities(tweets)
		temp = csr_matrix.transpose(self.auth)
		return np.asarray(temp.todense()).tolist()[0]
