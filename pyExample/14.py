class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        length = min([len(l) for l in strs])
        result = ""
        # if strs == [""]:
        #     return result

        for j in range(length):
            for i in range(len(strs)):
                if strs[i][j] == strs[0][j]:
                    e = 1
                else:
                    e = 0
                    break
            if e == 1:
                result += strs[0][j]
            else:
                return result
            
        return result



aa = ["flower","flow","flight"]
bb = ["c","acc","ccc"]


result = Solution()
print(result.longestCommonPrefix(bb))

# print(min([len(l) for l in aa]))
# print(aa[0][0] == aa[1][0])

