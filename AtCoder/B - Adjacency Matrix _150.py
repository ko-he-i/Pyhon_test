n= int(input())
a=[]
for _ in range(n):
    a.append(list(map(int, input().split())))

for i in range(n):
    v = []
    for j in range(n):
        if a[i][j]:
            v.append(j+1)
    
    print(*v)

n = int(input())
a = []

for _ in range(n):
    a.append(list(map(int, input().split())))

for i in range(n):
    v = []
    for j in range(n):
        if a[i][j]:
            v.append(j + 1)
    
    print(*v)