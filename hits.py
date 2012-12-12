import re
import json
import math
import time
import utils
import scipy as sp
import numpy as np
import networkx as nx
from collections import defaultdict
from scipy.sparse import *

class HITS(object):
	def __init__(self):
		#self.db = utils.connect_db("STOS", True)
		self.user_connections = defaultdict(set)
		self.graph = nx.DiGraph()
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
					temp = "@"
					if re.match("[\w]", token[1:]):
						for t in token[1:]:
							if not re.match("[\w]", t):
								break
							temp += t
					token = temp
					if len(token) > 1 and not re.match("[\d]", token[1]):
						if token not in self.user_to_id:
							self.user_to_id[token] = count
							self.id_to_user[count] = token
							count += 1
						key = "@" + tweet["screen_name"]
						self.user_connections[key].add(token)

	def set_A(self):
		A = lil_matrix((len(self.user_to_id.keys()),len(self.user_to_id.keys())))
		for user in self.user_connections:
			for mention in self.user_connections[user]:
				A[self.user_to_id[user],self.user_to_id[mention]] = 1
		return csr_matrix(A)
	
	def hubs_and_authorities(self, tweets):
		self.set_users(tweets)
		print "Users Set"
		A = self.set_A()
		AT = csr_matrix.transpose(A)
		self.auth = csr_matrix(np.ones((len(self.user_to_id.keys()),1)))
		self.hub = csr_matrix(np.ones((len(self.user_to_id.keys()),1)))
		test_auth = csr_matrix(np.zeros((len(self.user_to_id.keys()),1)))
		test_hub = csr_matrix(np.zeros((len(self.user_to_id.keys()),1)))
		print "Matrices Made"
		count = 0
		
		while not np.allclose(np.asarray(self.auth.todense()),np.asarray(test_auth.todense())) or not np.allclose(np.asarray(self.hub.todense()),np.asarray(test_hub.todense())):
			print count
			count += 1
			test_auth = self.auth.copy()
			test_hub = self.hub.copy()
			self.auth = AT.dot(self.hub)
			norm = sp.sqrt(sp.sum(sp.absolute(np.asarray(self.auth.todense()))**2))
			self.auth = csr_matrix(np.asarray(self.auth.todense()) / norm)
			self.hub = A.dot(self.auth)
			norm = sp.sqrt(sp.sum(sp.absolute(np.asarray(self.hub.todense()))**2))
			self.hub = csr_matrix(np.asarray(self.hub.todense()) / norm)
		print "Hubs and Authorities Done"
		del test_auth
		del test_hub
		temp = csr_matrix.transpose(self.hub)
		hubs = {}
		count = 0
		for hub in np.asarray(temp.todense()).tolist()[0]:
			hubs[self.id_to_user[count]] = hub
			count += 1
		temp = csr_matrix.transpose(self.auth)
		auths = {}
		count = 0
		for auth in np.asarray(temp.todense()).tolist()[0]:
			auths[self.id_to_user[count]] = auth
			count += 1
		print "Hubs and Authorities Set"
		count = 0
		for row in A:
			for item in row.nonzero()[1]:
				self.graph.add_edge(self.id_to_user[count], self.id_to_user[item], weight = 1 - hubs[self.id_to_user[item]])
			count += 1
		count = 0
		for row in AT:
			for item in row.nonzero()[1]:
				if not self.graph.has_edge(self.id_to_user[count], self.id_to_user[item]):
					self.graph.add_edge(self.id_to_user[count], self.id_to_user[item], weight = 1 - auths[self.id_to_user[item]])
			count += 1
		print "Saving Graphs"
		graph_dict = {}
		for edge in self.graph.edges():
			graph_dict[str(edge)] = self.graph.get_edge_data(edge[0], edge[1])
		f = open("data.json", "w")
		for edge in graph_dict:
			temp = {edge: graph_dict[edge]}
			f.write(json.dumps(temp))
			f.write("\n")
		print "Graph Saved"
	
	def get_matrix(self, tweets):
		self.set_users(tweets)
		return self.set_A()
	
	def get_hub(self, tweets):
		self.hubs_and_authorities(tweets)
		temp = csr_matrix.transpose(self.hub)
		hubs = {}
		count = 0
		for hub in np.asarray(temp.todense()).tolist()[0]:
			hubs[self.id_to_user[count]] = hub
			count += 1
		return hubs
		
	def get_auth(self, tweets):
		self.hubs_and_authorities(tweets)
		temp = csr_matrix.transpose(self.auth)
		auths = {}
		count = 0
		for auth in np.asarray(temp.todense()).tolist()[0]:
			auths[self.id_to_user[count]] = auth
			count += 1
		return auths

def main():
	tweets = utils.read_tweets()
	h = HITS()
	h.hubs_and_authorities(tweets)
	
if __name__ == "__main__":
	main()