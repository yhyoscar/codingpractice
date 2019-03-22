# Write an algorithm to print all ways of arranging eight queens on a chess board so that none of them share the same row, column or diagonal.

class TreeNode:
    def __init__(self, child={}, depth=None):
        self.depth = depth
        self.child = child
        return

    pass

def check_available(icol, irows=[], n=8):
    okrow = list(range(n))
    if len(irows) > 0:
        for j in range(len(irows)):
            if irows[j] in okrow:
                okrow.remove(irows[j])
            if irows[j] - (icol-j) >= 0 and irows[j]-(icol-j) in okrow:
                okrow.remove(irows[j]-(icol-j))
            if irows[j] + (icol-j) < n and irows[j]+(icol-j) in okrow:
                okrow.remove(irows[j]+(icol-j))
    return okrow

def build_tree(node, loc, N, results):
    if node.depth == N:
        #print(loc)
        results.append(loc)
    else:
        okrow = check_available(node.depth, loc, n=N)
        if len(okrow) > 0:
            for i in okrow:
                node.child[i] = TreeNode(depth=node.depth+1)
                build_tree(node.child[i], loc + [i], N, results)
    return


if __name__ == '__main__':
    root = TreeNode(depth=0)
    results=[]
    build_tree(root, [], 8, results)
    print(results, len(results))


