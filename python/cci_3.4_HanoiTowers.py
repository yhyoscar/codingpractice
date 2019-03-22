# In the classic problem of the Towers of Hanoi, you have 3 rods and N disks of different sizes which can slide onto any tower. The puzzle starts with disks sorted in ascending order of size from top to bottom (e.g., each disk sits on top of an even larger one). You have the following constraints:
# (A) Only one disk can be moved at a time.
# (B) A disk is slid off the top of one rod onto the next rod.
# (C) A disk can only be placed on top of a larger disk.
# Write a program to move the disks from the first rod to the last using Stacks.

# Recursion: S(n) = S(n-1)+1+S(n-1)+1+S(n-1) = 3S(n-1)+2; S(1) = 2
def hanoi_tower(N, direction=1):
    if N == 1:
        if direction > 0:
            print('1: 1->2')
            print('1: 2->3')
        else:
            print('1: 3->2')
            print('1: 2->1')
    else:
        hanoi_tower(N-1, direction=1)
        print(format(N)+': 1->2')
        hanoi_tower(N-1, direction=-1)
        print(format(N)+': 2->3')
        hanoi_tower(N-1, direction=1)
    return

if __name__ == '__main__':
    hanoi_tower(N=3)



