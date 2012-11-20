# script to test dijkstra's algorithm

import unittest
import dijkstra

# test graph for testing dijkstra's algroithm
# for a graphical representation, look at Dijkstra_Animation.gif that is located in this folder
# nodes 7 and 8 are not on the graph but only connect with each other
test_graph = {}
test_graph["1"] = {"2":7, "3":9, "6":14}
test_graph["2"] = {"1":7, "3":10, "4":15}
test_graph["3"] = {"1":9, "2":10, "4":11, "6":2}
test_graph["4"] = {"2":15, "3":11, "5":6}
test_graph["5"] = {"4":6, "6":9}
test_graph["6"] = {"1":14, "3":2, "5":9}
test_graph["7"] = {"8":10}
test_graph["8"] = {"7":10}

class TestDijkstra(unittest.TestCase):
	def test_shortest_path(self):
		# checks to see that the shortest path order
		# between point a and f is found
		order = dijkstra.shortestPath(test_graph, "1", "5")
		self.assertEqual(order, ["1","3","6","5"])
	
	def test_no_path(self):
		# checks that when there is no path between points,
		# an empty list is returned
		order = dijkstra.shortestPath(test_graph, "1", "7")
		self.assertEqual(order, [])
