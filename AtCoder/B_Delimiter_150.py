a = []
while True:
    ca = int(input())
    a.append(ca)
    if ca == 0:
        break

for i in range(len(a) -1, -1, -1):
    print(a[i])