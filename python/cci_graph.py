
# directed graph
class GraphNode:
    def __init__(self, id=None, parents=None, children=None):
        self.id = id
        self.parents = parents
        self.children = children
        self.visited = False
        return

    def visit(self):
        print('visit: ', self.id)
        self.visited = True
        return

    def traverse_DFS(self):
        if not self.visited: 
            self.visit()
            if (not (self.children is None)) and len(self.children)>0:
                for node in self.children:
                    if not node.visited:
                        node.traverse_DFS()
        return

    def traverse_BFS(self):
        if not self.visited:
            self.visit()
        if (not (self.children is None)) and len(self.children)>0:
            for node in self.children:
                if not node.visited:
                    node.visit()
        if (not (self.children is None)) and len(self.children)>0:
            for node in self.children:
                flagrec = False
                if (not (node.children is None)) and len(node.children)>0:
                    for child in node.children:
                        flagrec = flagrec or (not child.visited)
                if flagrec:
                    node.traverse_BFS()
        return

class Graph:
    def __init__(self, links={}):
        self.nodes = {}
        if len(links)>0:
            for i in links.keys():
                if not (i in self.nodes.keys()):
                    self.nodes[i] = GraphNode(id=i)
                if len(links[i])>0:
                    for j in links[i]:
                        if not (j in self.nodes.keys()):
                            self.nodes[j] = GraphNode(id=j)
                        
                        if self.nodes[j].parents is None:
                            self.nodes[j].parents = [self.nodes[i]]
                        else:
                            self.nodes[j].parents.append(self.nodes[i])
                        
                        if self.nodes[i].children is None:
                            self.nodes[i].children = [self.nodes[j]]
                        else:
                            self.nodes[i].children.append(self.nodes[j])
        return

    def resetvisit(self):
        if len(self.nodes)>0:
            for i in self.nodes.keys():
                self.nodes[i].visited = False
        return

if __name__ == '__main__':
    # links = {1:[2,5], 2:[1,3], 3:[], 4:[], 5:[2,3,4]}
    links = {1:[2,3], 2:[4,5], 3:[6,7]}
    g = Graph(links=links)
    g.nodes[1].traverse_DFS()
    g.resetvisit()
    for i in g.nodes.keys():
        print(g.nodes[i].id, g.nodes[i].visited)
    g.nodes[1].traverse_BFS()


