import pandas as pd
from math import inf
import numpy as np


def read_graph(graph_name: str = 'graph.csv'):
    data = open(graph_name)
    graph_df = pd.read_csv(data)
    shape = (len(graph_df.columns), len(graph_df.columns))
    graph = np.full(shape, inf)

    for index, row in graph_df.iterrows():
        sub_index = 0
        for element in row:
            value = element
            if element == "-":
                value = inf
            graph[index][sub_index] = value
            sub_index += 1
    return graph


def find_min_edge(graph):
    min_edge = inf
    min_edge_index = 0
    min_edge_sub_index = 0
    for index in range(len(graph)):
        for sub_index in range(index):
            min_edge = min(min_edge, graph[index][sub_index])
            if min_edge == graph[index][sub_index]:
                min_edge_index = index
                min_edge_sub_index = sub_index
    return min_edge, [min_edge_index, min_edge_sub_index]


def all_verteces(graph=read_graph()):
    return [value for value in range(len(graph))]
