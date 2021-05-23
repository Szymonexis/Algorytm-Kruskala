import numpy as np
from random import randint
import additional_funcs
from math import inf
from copy import deepcopy

# The time complexity of Kruskal's Algorithm is: O(n log n) where n - amount of edges
# The time complexity of sorted() is: O(n log n) where n - amount of elements to sort


class Graph:
    def __init__(self, verteces):
        self.num_of_ver = verteces
        self.graph = []
        self.minimal_span_tree = []

    def add_edge(self, edge_a, edge_b, weight):
        self.graph.append([edge_a, edge_b, weight])

    def __repr__(self):
        return_str = ""
        counter = 0
        for value in self.graph:
            return_str += f"{counter}:{str(value).rjust((5 + len(str(value)) - len(str(counter))), ' ')}\n"
            counter += 1

        return_str += f"Minimal spanning tree:\n{self.minimal_span_tree}\n"
        return_str += f"Minimal cost: {self.get_minimal_cost()}"
        return return_str

    # searching for a parent of a given vertex
    def find_parent(self, parent, index):
        if parent[index] == index:
            return index
        return self.find_parent(parent, parent[index])

    # connects an x tree to y tree or y tree to x tree
    def do_union(self, parent, rank, x, y):
        xroot = self.find_parent(parent, x)
        yroot = self.find_parent(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    # algorithm
    def kruskal(self):
        self.graph = sorted(self.graph, key=lambda item: item[2])  # sorting regards to weight
        # --------------------------------------------------------------------------------------|
        # The sort is O(n log n) both on average and in the worst case                          |
        # provided that itemgetter(0) is O(1) which it is in our case as it is:                 |
        #       key=lambda item: item[2]                                                        |
        # --------------------------------------------------------------------------------------|
        # It's Timesort - a comparison sorting algorithm based on merge sort and insertion sort |
        # and because of this it can't do better than O(n log n)                                |
        # --------------------------------------------------------------------------------------|
        result = []
        index, iteration = 0, 0
        parent = []     # list of parents (initially all vertices are on the same level - all parents)
        rank = []       # rank for each vertex - higher rank == lower in the tree
        for vertex in range(self.num_of_ver):
            parent.append(vertex)
            rank.append(0)
        while iteration < self.num_of_ver - 1:
            ver_a, ver_b, weight = self.graph[index]    # unpacking edge
            index += 1
            x = self.find_parent(parent, ver_a)
            y = self.find_parent(parent, ver_b)
            if x != y:  # if x and y are not from the same tree
                iteration += 1
                result.append([ver_a, ver_b, weight])
                self.do_union(parent, rank, x, y)
        self.minimal_span_tree = result

    def get_minimal_cost(self):
        value = 0
        for entry in self.minimal_span_tree:
            value += entry[2]
        if value == 0:
            value = None
        return value

    def get_min_span_tree(self):
        return deepcopy(self.minimal_span_tree)


graph = Graph(len(additional_funcs.all_verteces()))
graph_csv = additional_funcs.read_graph()
for index in range(len(graph_csv)):
    for sub_index in range(len(graph_csv)):
        if graph_csv[index][sub_index] < inf:
            graph.add_edge(index, sub_index, graph_csv[index][sub_index])
graph.kruskal()

graph_maze = np.full((10, 10), 3)
graph2 = Graph(10)
for index in range(len(graph_maze)):
    for sub_index in range(len(graph_maze)):
        graph_maze[index][sub_index] = randint(0, 1000)
        graph2.add_edge(index, sub_index, graph_maze[index][sub_index])
graph2.kruskal()

for index in range(len(graph_maze)):
    for sub_index in range(len(graph_maze)):
        if [index, sub_index, graph_maze[index][sub_index]] in graph2.minimal_span_tree:
            graph_maze[index][sub_index] = 0
        else:
            graph_maze[index][sub_index] = 1
print(graph_maze)
print(graph2.graph)


