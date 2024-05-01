class Solution:
    def letterCombinations(self, digits: str):
        direct = {'2':['a','b','c'],
                 '3':['d','e','f'],
                 '4':['g','h','i'],
                 '5':['j','k','l'],
                 '6':['m','n','o'],
                 '7':['p','q','r','s'],
                 '8':['t','u','v'],
                 '9':['w','x','y','z']}
        result = []
        self.backtracking(0, digits, direct, [], result)
        return result
        
    def backtracking(self, Index, digits, direct, path, result):
        if len(path) == len(digits):
            result.append(''.join(path))
            return
        
        
        val = direct[digits[Index]]
        for j in val:
            path.append(j)
            self.backtracking(Index + 1, digits, direct, path, result)
            path.pop()
    

result = Solution()
digits = "23"
print(result.letterCombinations(digits))