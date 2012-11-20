# script to test dijkstra's algorithm

import unittest
import dijkstra

# test graph for testing dijkstra's algroithm
test_graph = {}
test_graph["a"] = {"b":7, "c":14, "d":9}
test_graph["b"] = {"a":7, "d":10, "e":15}
test_graph["c"] = {"a":14, "d":2, "f":9}
test_graph["d"] = {"a":9, "b":10, "c":2, "e":11}
test_graph["e"] = {"b":15, "d":11, "f":6}
test_graph["f"] = {"c":9, "d":6}
test_graph["g"] = {"h":10}
test_graph["h"] = {"g":10}

class TestDijkstra(unittest.TestCase):
	def test_shortest_path(self):
		# checks to see that the shortest path order
		# between point a and f is found
		order = dijkstra.shortestPath(test_graph, "a", "f")
		self.assertEqual(order, ["a","d","c","f"])
	
	def test_no_path(self):
		# checks that when there is no path between points,
		# an empty list is returned
		order = dijkstra.shortestPath(test_graph, "a", "g")
		self.assertEqual(order, [])
