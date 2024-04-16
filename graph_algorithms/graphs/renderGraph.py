# this script converts representation of graph into .png file

import graphviz

def print_digraph_from_matrix(adj_matrix: list[list[int]], name):
    # Create a directed graph
    g = graphviz.Digraph(format="png")

    # Add nodes
    for i in range(len(adj_matrix)):
        g.node(str(i))

    # Add edges
    for i in range(len(adj_matrix)):
        for j in range(len(adj_matrix[i])):
            if adj_matrix[i][j] == 1:
                g.edge(str(i), str(j))

    # Render the graph
    g.render(f'{name}')

def print_digraph_from_list(graph: list[list[int]], name):
    g = graphviz.Digraph(format="png")

    for v in range(len(graph)):
        g.node(str(v))

    for vertex in range(len(graph)):
        for neighbour in graph[vertex]:
            g.edge(str(vertex), str(neighbour))

    g.render(f"{name}")

def print_graph_from_list(graph: list[list[int]], name):
    g = graphviz.Graph(format="png")

    for v in range(len(graph)):
        g.node(str(v))

    edges = []

    for vertex in range(len(graph)):
        for neighbour in graph[vertex]:
            if (neighbour, vertex) not in edges:
                edges.append((vertex, neighbour))
                g.edge(str(vertex), str(neighbour))

    g.render(f"{name}")

if __name__ == "__main__":
    # paste here graph reprezentation
    graph15 =  [[1,2,3],
                [0,2],
                [0,1,4,5,6],
                [0,4],
                [2,3,6],
                [2,6],
                [2,4,5]]

    # call function for choosen implementation
    print_graph_from_list(graph15, "graph15")

    # after running this file graph representation will be rendered