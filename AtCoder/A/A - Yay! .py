# 解答
s=input()
a = s[0]
b = s[1]
c = s[2]
if s[0] == s[1]:
    ans = s[0]
elif s[0] == s[2]:
    ans = s[0]
elif s[1] == s[2]:
    ans = s[1]

for i in range(len(s)):
    if s[i] != ans:
        print(i + 1)

# 答え
s = input()
n = len(s)

for i in range(n):
    diff = True
    for j in range(n):
        if i != j and s[i] == s[j]:
            diff = False
    if diff == True:
        print(i +1)