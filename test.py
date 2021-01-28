#Continuing Education - Search Algorithms
#Tests written by Peter Jang

import unittest
from search import LinearSearch, BinarySearch, BreadthFirstSearch, DepthFirstSearch

class TestLinearSearch(unittest.TestCase):
    def test_simple1(self):
        short_list = [5,3,1,2,7,6,9,8]
        self.assertEqual(LinearSearch(short_list, 6), ([5, 3, 1, 2, 7, 6], 5))
    def test_simple2(self):
        short_list = [1,7,9,4,5,6,2,3,8]
        self.assertEqual(LinearSearch(short_list, 1), ([1], 0))
    def test_simple3(self):
        short_list = [1,2,3,4,5,6,7,8,9]
        self.assertEqual(LinearSearch(short_list, 13), ([1,2,3,4,5,6,7,8,9], None))

class TestBinarySearch(unittest.TestCase):
    def test_binary1(self):
        binary_list = [1,2,3,4,5,6,7]
        self.assertEqual(BinarySearch(binary_list, 3), ([4, 2, 3], 2))
    def test_binary2(self):
        binary_list = [1,2,3,4,5,6,7]
        self.assertEqual(BinarySearch(binary_list, 5), ([4, 6, 5], 4))
    def test_binary3(self):
        binary_list = [2,6,12,15,18,23,42]
        self.assertEqual(BinarySearch(binary_list, 19), ([15, 23, 18], None))

class TestBreadthFirstSearch(unittest.TestCase):
    def test_breadth1(self):
        graph = {
            'A': ['B', 'C'],
            'B': ['D', 'E'],
            'C': ['F', 'G'],
            'D': ['H', 'I'],
            'E': ['J', 'K'],
            'F': ['L', 'M'],
            'G': ['N', 'O'],
        }
        self.assertEqual(BreadthFirstSearch(graph, 'A', 'M'), ([['A', 'B'], ['A', 'C'], ['A', 'B', 'D'], ['A', 'B', 'E'], 
        ['A', 'C', 'F'], ['A', 'C', 'G'], ['A', 'B', 'D', 'H'], ['A', 'B', 'D', 'I'], ['A', 'B', 'E', 'J'], ['A', 'B', 'E', 'K'], 
        ['A', 'C', 'F', 'L'], ['A', 'C', 'F', 'M']], ['A', 'C', 'F', 'M']))
    def test_breadth2(self):
        graph = {
            'A': ['B', 'C'],
            'B': ['D', 'E'],
            'C': ['F', 'G'],
            'D': ['H', 'I'],
            'E': ['J', 'K'],
            'F': ['L', 'M'],
            'G': ['N', 'O'],
        }
        self.assertEqual(BreadthFirstSearch(graph, 'A', 'E'), ([['A', 'B'], ['A', 'C'], ['A', 'B', 'D'], ['A', 'B', 'E']], ['A', 'B', 'E']))
    def test_breadth3(self):
        graph = {
            'A': ['B', 'C'],
            'B': ['D', 'E'],
            'C': ['F', 'G'],
            'D': ['H', 'I'],
            'E': ['J', 'K'],
            'F': ['L', 'M'],
            'G': ['N', 'O'],
        }
        self.assertEqual(BreadthFirstSearch(graph, 'A', 'P'), ([['A', 'B'], ['A', 'C'], ['A', 'B', 'D'], ['A', 'B', 'E'], ['A', 'C', 'F'], 
        ['A', 'C', 'G'], ['A', 'B', 'D', 'H'], ['A', 'B', 'D', 'I'], ['A', 'B', 'E', 'J'], ['A', 'B', 'E', 'K'], ['A', 'C', 'F', 'L'], 
        ['A', 'C', 'F', 'M'], ['A', 'C', 'G', 'N'], ['A', 'C', 'G', 'O']], None))

class TestDepthFirstSearch(unittest.TestCase):
    def test_depth1(self):
        graph = {
            'A': ['B', 'C'],
            'B': ['D', 'E'],
            'C': ['F', 'G'],
            'D': ['H', 'I'],
            'E': ['J', 'K'],
            'F': ['L', 'M'],
            'G': ['N', 'O'],
        }
        self.assertEqual(DepthFirstSearch(graph, 'A', 'K'), ['A', 'B', 'E', 'K'])
    
    def test_depth2(self):
        graph = {
            'A': ['B', 'C'],
            'B': ['D', 'E'],
            'C': ['F', 'G'],
            'D': ['H', 'I'],
            'E': ['J', 'K'],
            'F': ['L', 'M'],
            'G': ['N', 'O'],
        }
        self.assertEqual(DepthFirstSearch(graph, 'A', 'M'), ['A', 'C', 'F', 'M'])

    def test_depth3(self):
        graph = {
            'A': ['B', 'C'],
            'B': ['D', 'E'],
            'C': ['F', 'G'],
            'D': ['H', 'I'],
            'E': ['J', 'K'],
            'F': ['L', 'M'],
            'G': ['N', 'O'],
        }
        self.assertEqual(DepthFirstSearch(graph, 'A', 'Q'), None)

if __name__ == '__main__':
    unittest.main()