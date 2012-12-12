# script to test a* algorithm

import unittest
import networkx as nx

# test graph for testing a* algroithm, which is a derivative of Dijkstra's algorithm
# for a graphical representation, look at Dijkstra_Animation.gif that is located in this folder
# nodes 7 and 8 are not on the graph but only connect with each other
graph = nx.DiGraph()
graph.add_edge("1", "2", "weight" = 7)
graph.add_edge("1", "3", "weight" = 9)
graph.add_edge("1", "6", "weight" = 14)
graph.add_edge("2", "1", "weight" = 7)
graph.add_edge("2", "3", "weight" = 10)
graph.add_edge("2", "4", "weight" = 15)
graph.add_edge("3", "1", "weight" = 9)
graph.add_edge("3", "2", "weight" = 10)
graph.add_edge("3", "4", "weight" = 11)
graph.add_edge("3", "6", "weight" = 2)
graph.add_edge("4", "2", "weight" = 15)
graph.add_edge("4", "3", "weight" = 11)
graph.add_edge("4", "5", "weight" = 6)
graph.add_edge("5", "4", "weight" = 6)
graph.add_edge("5", "6", "weight" = 9)
graph.add_edge("6", "1", "weight" = 14)
graph.add_edge("6", "3", "weight" = 2)
graph.add_edge("6", "5", "weight" = 9)

class TestAStar(unittest.TestCase):
	def test_shortest_path(self):
		# checks to see that the shortest path order
		# between point a and f is found
		order = nx.astar(graph, "1", "5")
		self.assertEqual(order, ["1","3","6","5"])
