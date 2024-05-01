a = '''5
1627845600,client1,factorA,10
1627845605,client2,factorB,15
1627845610,client1,factorA,5
1627845615,client1,factorB,8
1627845620,client2,factorB,20
2
factorA,5
factorB,7'''

b = a.split('\n')

n = int(b[0])
b_n = b[1 : n + 1]
# print(b_n)
m = int(b[n + 1])
# print(m)
b_m = b[n + 2 : n + 2 + m]
# print(b_m)

seen = set()
logs = []
for i in range(n):
    time, client, factor, dur = b_n[i].split(',')
    key = time + client + factor
    if key not in seen:
        logs.append((time, client, factor, int(dur)))
        seen.add(key)

print(logs)
# print(seen)

dict = {}
for m in range(m):
    factor, value = b_m[m].split(',')
    dict[factor] = int(value)

print(dict)

bills = {}
for time, client, factor, dur in logs:
    # print(time, client, factor, dur)
    if client not in bills:
        bills[client] = 0
    if dur < 0 or dur > 100:
        dur = 0
    bills[client] += dict[factor] * dur

ans = sorted(bills.items())
for cid, bill in ans:
    print(f'{cid},{bill}')