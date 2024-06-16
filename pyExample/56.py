class Solution:
    def merge(self, intervals):
        i = 0
        l = len(intervals) - 1
        intervals = sorted(intervals, key = lambda x : x[0])
        while i + 1 <= l:
            if intervals[i][1] >= intervals[i + 1][0]:
                num_min = min(intervals[i][0], intervals[i + 1][0])
                num_max = max(intervals[i][1], intervals[i + 1][1])
                intervals[i] = [num_min, num_max]
                del intervals[i + 1]
                l -= 1
            else:
                i += 1
        return intervals
    
result = Solution()
nums = [[1,3],[2,6],[8,10],[15,18]]
print(result.merge(nums))