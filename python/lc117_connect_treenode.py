# lc 117

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root, flag=1):
        if flag==1:
            cur = root
            head = None
            pre = None
            
            while cur is not None:
                # each level
                while cur is not None:
                    if cur.left is not None:
                        if pre is None:
                            head = cur.left
                        else:
                            pre.next = cur.left
                        pre = cur.left
                    if cur.right is not None:
                        if pre is None:
                            head = cur.right
                        else:
                            pre.next = cur.right
                        pre = cur.right
                    cur = cur.next
                # the next level
                cur = head
                head = None
                pre = None
                
            
        if flag==2:
            if root is not None:
                queue = [root]
                depth = [0]
                while len(queue)>0:
                    if depth[0] == depth[-1]:
                        for i in range(len(queue)-1):
                            queue[i].next = queue[i+1]                        
                    p = queue.pop(0)
                    d = depth.pop(0)
                    if p.left is not None:
                        queue.append(p.left)
                        depth.append(d+1)
                    if p.right is not None:
                        queue.append(p.right)
                        depth.append(d+1)
        return
