# class Solution:
    # def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
    #     d = []
    #     value = []
    #     for i in strs:
    #         if sorted(i) not in d:
    #             d.append(sorted(i))
        
    #     value = [[] for j in range(len(d))]

    #     for j in range(len(d)):
    #         for i in strs:
    #             if sorted(i) == d[j]:
    #                 value[j].append(i)

    #     return value
    
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        d = {}
        for i in strs:
            same = "".join(sorted(i))
            if same not in d:
                d[same] = [i]
            else:
                d[same].append(i)

        result = d.values()

        return list(result)


result = Solution()
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(result.groupAnagrams(strs))

# strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# d = []
# i = 0
# d.append(sorted(strs[0]))
# print(d)
# print(['a', 'e', 't'] in d)
# print(sorted(strs[0]))

# for i in strs:
#     d[sorted(i)] = 1
# print(d)