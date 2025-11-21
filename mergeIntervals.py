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
