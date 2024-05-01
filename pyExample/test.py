class DisjointUnionFindSet:
    def __init__(self, n):
        self.rank = [1] * n  # 秩，在并查集树上的深度
        self.f = list(range(n))  # 根节点，初始化都指向自身

    def find(self, x: int) -> int:
        if self.f[x] == x:  # 如果本身是根节点就直接返回自身
            return x
        self.f[x] = self.find(self.f[x])  # 父节点设为根节点
        return self.f[x]  # 返回父节点（也就是根节点）

    def merge(self, x: int, y: int) -> bool:
        fx, fy = self.find(x), self.find(y)  # 先找到两个根节点
        if fx == fy:  # 根节点相同则不需合并，已在同一个树内
            return False

        if self.rank[fx] < self.rank[fy]:  # 比较秩，保证深度大的作为合并的父节点
            fx, fy = fy, fx

        self.rank[fx] += self.rank[fy]  # 合并秩
        self.f[fy] = fx  # 秩小的将秩大的作为父节点
        return True
    
s = DisjointUnionFindSet(5)
# print(s.find(1))
s.merge(0, 1)
print(s.find(1))
print(s.f)
print(s.rank)
