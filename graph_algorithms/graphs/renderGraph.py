# this script converts representation of graph into .png file

import graphviz

def print_graph_from_matrix(adj_matrix: list[list[int]], name):
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

def print_graph_from_list(graph: list[list[int]], name):
    g = graphviz.Digraph(format="png")

    for v in range(len(graph)):
        g.node(str(v))

    for vertex in range(len(graph)):
        for neighbour in graph[vertex]:
            g.edge(str(vertex), str(neighbour))

    g.render(f"{name}")

if __name__ == "__main__":
    # paste here graph reprezentation
    graph11 = [[1,5],
               [2],
               [3],
               [4],
               [0],
               [6],
               [7],
               [8],
               [9],
               [10],
               [5]]

    # call function for choosen implementation
    print_graph_from_list(graph11, "graph11")

    # after running this file graph representation will be rendered