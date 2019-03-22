
class Graph:
    def __init__(self, n):
        self.nodes = {i:set() for i in range(n)}
        return
    def connect(self, i,j):
        self.nodes[i].add(j)
        self.nodes[j].add(i)
        return
    def find_all_distances(self, i):
        dis = {i:0 for i in range(n)}
        visited = {i:False for i in range(n)}
        q = [i]
        visited[i] = True 
        while len(q)>0:
            print(q)
            x = q.pop(0)
            for j in self.nodes[x]:
                if not visited[j]:
                    dis[j] = dis[x] + 6
                    q.append(j)
                    visited[j] = True
        
        for j in sorted(dis.keys()):
            if dis[j] == 0: dis[j] = -1
            if j != i: print(dis[j], end=' ') 
        print('')
        return

with open('input') as fid:
    t = int(fid.readline())
    for i in range(t):
        n,m = [int(value) for value in fid.readline().split()]
        graph = Graph(n)
        for i in range(m):
            x,y = [int(x) for x in fid.readline().split()]
            graph.connect(x-1,y-1) 
        for i in graph.nodes:
            print(i, sorted(graph.nodes[i]))
        s = int(fid.readline())
        graph.find_all_distances(s-1)
