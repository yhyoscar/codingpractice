# Given a directed graph, design an algorithm to find out whether there is a route between two nodes.

from cci_graph import GraphNode, Graph

# traverse the graph to check if there is a route
def isroute(g, id1, id2):
    if (id1 in g.nodes.keys()) and (id2 in g.nodes.keys()):
        g.nodes[id1].traverse_DFS()
        return g.nodes[id2].visited
    else:
        return False


if __name__ == '__main__':
    links = {1:[2,5], 2:[1,3], 3:[4], 4:[], 5:[2,3,4], 6:[1,4]}
    g = Graph(links=links)
    print(isroute(g, 1, 6))
    g.resetvisit()
    print(isroute(g, 6, 1))

