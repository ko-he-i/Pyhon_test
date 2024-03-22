N = int(input())
x_score = 0
y_score = 0
for i in range(N):
    x,y = map(int, input().split())
    x_score += x
    y_score += y

if x_score > y_score:
    print('Takahashi')
elif x_score < y_score:
    print('Aoki')
elif x_score == y_score:
    print('Draw')