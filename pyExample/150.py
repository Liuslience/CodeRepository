class Solution:
    def evalRPN(self, tokens) -> int:
        stack = []
        for i in tokens:
            if i.isdigit():
                stack.append(int(i))
            elif i.startswith('-'):
                stack.append(-1 * int(i[1:]))
            elif i == '+':
                stack.append(stack.pop() + stack.pop())
            elif i == '-':
                a = stack.pop()
                b = stack.pop()
                stack.append(b - a)
            elif i == '*':
                stack.append(stack.pop() * stack.pop())
            elif i == '/':
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b / a))

            print(stack)
        
        return int(stack[0])
    
result = Solution()
tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(result.evalRPN(tokens))