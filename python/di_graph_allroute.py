# Find all routes in a directed graph

def addroute(a='a', b='b', rall=dict()):
    if a in rall:
        rall[a].append(b)
    else:
        rall[a] = [b]
    return 

def findallroute(s, t, rall):
    visited = {x:False for x in rall}
    childnum = {x:len(rall[x]) for x in rall}
    vchild = {x:0 for x in rall}
    path = [s]
    visited[s] = True
    while len(path) > 0:
        print(path, visited, vchild)
        if path[-1] == t:
            print(path)
            path.pop()
            visited[t] = False
            vchild[t] = 0
        else:
            if vchild[path[-1]] < childnum[path[-1]]:
                if not visited[rall[path[-1]][vchild[path[-1]]]]:
                    path.append(rall[path[-1]][vchild[path[-1]]])
                    visited[path[-1]] = True
                    vchild[path[-2]] += 1 
                else:
                    vchild[path[-1]] += 1 
            else:
                x = path.pop()
                visited[x] = False
                vchild[x] = 0
    return


def findallroute2(s='a', t='c', rall={}):
    visited = {x:False for x in rall}
    path = []
    findallroute_rec(s, t, visited, path, rall)
    return

def findallroute_rec(s, t, visited, path, rall):
    visited[s] = True
    path.append(s)
    print(s,t, path)
    
    if s==t:
        print(path)
    else:
        for x in rall[s]:
            if not visited[x]:
                findallroute_rec(x, t, visited, path, rall)
    
    path.pop()
    visited[s] = False
    return

rall = dict()
addroute('0','1',rall)
addroute('0','2',rall)
addroute('0','3',rall)
addroute('1','3',rall)
addroute('2','0',rall)
addroute('2','1',rall)
rall['3'] = []

rall = {x:list(rall[x]) for x in rall}
findallroute(s='2', t='3', rall=rall)

