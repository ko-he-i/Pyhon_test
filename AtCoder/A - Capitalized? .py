s = input()
ans = False
if s[0].isupper():
    ans = True

for i in range(1, len(s)):
    if s[i].isupper():
        ans = False
        break

if ans:
    print('Yes')
else:
    print('No')

# answer 1
S=input()
ans=S[0].isupper()
for i in range(1, len(S)):
    ans &= S[i].islower()
print('Yes' if ans else 'No')