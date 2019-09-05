class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 0:
            return []
        else:
            si = sorted(intervals, key=lambda x: x[0])
            merged = [[si[0][0], si[0][1]]]
            j = 0
            for i in range(len(intervals)-1):
                if merged[j][1] < si[i+1][0]:
                    merged.append([si[i+1][0], si[i+1][1]])
                    j += 1
                else:
                    merged[j][1] = max(si[i+1][1], merged[j][1])

            return merged

