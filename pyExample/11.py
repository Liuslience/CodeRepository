class Solution:
    def maxArea(self, height: list[int]) -> int:
        x = 0
        y = len(height) - 1
        v = []
        for i in range(len(height)):
            v.append(min(height[x], height[y]) * (y - x))
            if height[x] < height[y]:
                x += 1
            elif x + 1 == y:
                break
            else:
                y -= 1
        return max(v)




result = Solution()
nums = [1,8,6,2,5,4,8,3,7]
print(result.maxArea(nums))