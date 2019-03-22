# words analysis program

# Functions: 
# 1. Read the top 10000 English words and build a trie;
# 2. Traverse the trie to get the words list;
# 3. Search a given word;

class Node:
    def __init__(self, id=None, child=None):
        self.id = id
        self.child = child
        return

def add_word(root, word, id):
    if word == '' and id >= 0:
        root.id = id
    else:
        if root.child is None:
            root.child = {word[0]:Node()}
        else:
            if word[0] not in root.child.keys():
                root.child[word[0]] = Node()
        add_word(root.child[word[0]], word[1:], id)
    return

def build_trie(wlist={}):
    if len(wlist) == 0:
        return None
    else:
        root = Node(id = -1)
        for i in wlist.keys():
            add_word(root, wlist[i], i)
        return root

def search_word(root, word):
    if word == '':
        return root.id
    else:
        if (root.child is not None) and (word[0] in root.child):
            return search_word(root.child[word[0]], word[1:])
        else:
            return None

def traverse_trie(root, wlist, word):
    if root.child is None:
        wlist[word] = root.id
    else:
        for c in root.child:
            traverse_trie(root.child[c], wlist, word+c)
    return 

def readwords(fn='google-10000-english-usa.txt', minline=0, maxline=9999):
    with open(fn, 'r') as fid:
        wlist = fid.readlines()
    return {i:wlist[i].strip('\n') for i in range(minline, maxline+1)}


if __name__ == '__main__':
    wlist = readwords(minline=0, maxline=7)
    print(len(wlist))
    print(wlist)
    root = build_trie(wlist)
    print('search: ', search_word(root, 'to') )
    wtable = {}
    traverse_trie(root, wtable, '')
    print(wtable)

