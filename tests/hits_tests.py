# script to test the HITS algorithm

import unittest
import hits
import numpy as np
from scipy.sparse import *
from decimal import Decimal

tiny_corpus = [
	{"text": "Hey @node2 @node3 and @node4 we should work on the hw together", "screen_name": "node1"},
	{"text": "I'm game, what about @node3 and @node4?", "screen_name": "node2"},
	{"text": "I just can't work with @node2!", "screen_name": "node3"},
]

class TestHits(unittest.TestCase):
	def test_matrix(self):
		# test matrix made by user mentions
		h = hits.HITS()
		matrix = h.get_matrix(tiny_corpus)
		test_mat = lil_matrix((4,4))
		test_mat[0,1] = 1
		test_mat[0,2] = 1
		test_mat[0,3] = 1
		test_mat[1,2] = 1
		test_mat[1,3] = 1
		test_mat[2,1] = 1
		self.assertEqual(True, np.array_equal(np.asarray(test_mat.todense()), np.asarray(matrix.todense())))
	
	def test_hubs(self):
		# test the hubs values
		h = hits.HITS()
		hubs = h.get_hub(tiny_corpus)
		count = 0
		test_hub = [.7887, .5774, .2113, 0]
		for hub in hubs:
			self.assertEqual(test_hub[count], float(Decimal(str(hub)).quantize(Decimal("0.0001"))))
			count += 1
	
	def test_auth(self):
		# test the authority values
		h = hits.HITS()
		auths = h.get_auth(tiny_corpus)
		count = 0
		test_auth = [0, .4597, .6280, .6280]
		for auth in auths:
			self.assertEqual(test_auth[count], float(Decimal(str(auth)).quantize(Decimal("0.0001"))))
			count += 1
