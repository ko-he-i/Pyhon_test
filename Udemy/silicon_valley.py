# メイン関数
def main():
    # 入力を受け取る
    N, v = map(int, input().split())
    a = list(map(int, input().split()))
    
    # 線形探索
    exist = False   # 初期値は False に
    for num in a:
        if num == v:
            exist = True  # 見つかったらフラグを立てる
            break  # 一度見つかれば探索を終了
    
    # 結果出力
    if exist:
        print("Yes")
    else:
        print("No")

# プログラムのエントリーポイントを指定
if __name__ == "__main__":
    main()
