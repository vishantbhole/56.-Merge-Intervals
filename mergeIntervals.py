#56. Merge Intervals

from typing import List


class Solution:
    def mergeIntervals(self, intervals: List[List[int]]) -> List[List[int]]:
        #O(nlogn)
        intervals.sort(key = lambda i : i[0])
        output = [intervals[0]]
        for start, end in intervals[1:]:
            lastEnd = output[-1][1]

            if start <= lastEnd:
                output[-1][1] = max(lastEnd, end)
            else:
                output.append([start,end])
        return output

if __name__ == "__main__":
    sol = Solution()
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    print("Output is : ", sol.mergeIntervals(intervals))
    
    intervals2 = [[1,4],[4,5]]
    print("Output is : ", sol.mergeIntervals(intervals2))
