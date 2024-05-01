class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = []
        left, right = 0, len(nums) - 1

        for i in range(len(nums) - 2):
            if nums[i] > 0 : break
            if i > 0 and nums[i] == nums[i - 1]: continue
            j, k = i + 1, len(nums) - 1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s > 0:
                    k -= 1
                    while (j < k) & (nums[k + 1] == nums[k]):k -= 1
                elif s < 0:
                    j += 1
                    while (j < k) & (nums[j - 1] == nums[j]):j += 1
                else:
                    result.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while (j < k) & (nums[k + 1] == nums[k]):k -= 1
                    while (j < k) & (nums[j - 1] == nums[j]):j += 1

        return result

result = Solution()
nums = [-2,0,0,2,2]
print(result.threeSum(nums))