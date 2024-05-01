x = 1221
x = str(x)

x = [int(z) for z in x]
print(len(x))

b = 0
if len(x) % 2 == 0:
    for i in [0, len(x)//2 - 1]:
        if x[i] == x[len(x) - i - 1]:
            pass
        else:
            b = 1
else:
    for i in [0, (len(x) - 1) // 2 - 1]:
        if x[i] == x[len(x) - i - 1]:
            pass
        else:
            b = 1

print(b)




