x = int(input())
ans = x/10
if ans.is_integer():
    print(ans)
elif ans.isdigit():
    ans = int(ans)
    print(ans + 1)
elif ans.isdigit() == False:
    ans = int(ans)
    print(ans - 1)