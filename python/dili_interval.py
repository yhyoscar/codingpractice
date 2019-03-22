

def merge(intervals):
    intervals_sort = sorted(intervals, key=lambda x: x[0])
    merged = [[intervals_sort[0][0], None]]
    for i in range(len(intervals)-1):
        if intervals_sort[i][1] < intervals_sort[i+1][0]:
            merged[-1][1] = intervals_sort[i][1]
            merged.append([intervals_sort[i+1][0], None])
    merged[-1][1] = intervals_sort[-1][1]
    return merged

def complement(intervals):
    comp = []
    if intervals[0][0] != float('-inf'):
        comp = [[float('-inf'), intervals[0][0]]]
    for i in range(len(intervals)-1):
        comp.append( [intervals[i][1], intervals[i+1][0]] )
    if intervals[-1][1] != float('inf'):
        comp.append([intervals[-1][1], float('inf')])
    return comp

def check_available(intervals1, intervals2):
    s1 = merge(intervals1); s2 = merge(intervals2)
    print(s1)
    print(s2)
    print(complement(s1))
    print( merge(complement(s1) + s2) )
    return complement(merge(complement(s1) + s2))

intervals1 = [[1,3],   [2,4], [6,8], [7,9], [11,12]]
intervals2 = [[0,2], [3,4.5], [5,8], [8,10]]
print( check_available(intervals1, intervals2) )


