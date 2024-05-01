def find(x, p):
    if p[x] == x:
        return x
    p[x] = find(p[x], p)
    return p[x]
    
def merge(x, y, s, g, p):
    fx, fy = find(x, p), find(y, p)
    if fx == fy:
        s[fy] += g
    else:
        p[fx] = fy
        s[fy] += s[fx] + g

a = '''5
0 0 50 0 0
0 0 0 25 0
50 0 0 0 15
0 25 0 0 0
0 0 15 0 0'''

b = a.split('\n')
# print(b)

n = int(b[0])
b_n = b[1 : n + 1]
nums = []
for i in range(n):
    nums.append(list(map(lambda x : int(x), b_n[i].split(' '))))
# print(nums)

p = list(range(n))
s = [0] * n

for i in range(n):
    for j in range(n):
        if nums[i][j] != 0:
            merge(i, j, s, nums[i][j], p)

print(s)
print(p)
res = []
for i in range(n):
    if p[i] == i:
        res.append(s[i] // 2)

res.sort(reverse=True)
print(*res)
            





