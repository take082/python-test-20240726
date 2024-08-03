import time
import sys
from doctest import testmod


def trib(n):
    """フィボナッチ数列を拡張した『トリボナッチ』数を返す
    args:
        n: 何番目のトリボナッチ数を求めるか
    returns:
        n番目のトリボナッチ数

    トリボナッチ数は以下のルールで生成される数である。
    * nは0からはじまるものとする
    * 初項(0)〜第3項(2)までは1とする
    * 第4項(3)以降は、直前の3つの数の和となる
    * 本関数定義においては、入力値は0〜100の範囲とする
        * それ以外の入力値は想定しなくて良い
    たとえば
    >>> trib(2)
    1
    >>> trib(3) # 1 + 1 + 1 = 3
    3
    >>> trib(4) # 3 + 1 + 1 = 5
    5
    >>> trib(5) # trib(4) + trib(3) + trib(2) = 5 + 3 + 1 = 9
    9
    >>> trib(16)
    7473
    """
    # 初項(0)〜第3項(2)までは1とする
    if n == 0 or n == 1 or n == 2:
        return 1

    # 再帰を使って計算する
    return trib(n - 1) + trib(n - 2) + trib(n - 3)

# 単純に起動した場合にテストをする
if __name__ == "__main__":
    print("ロジックのテストを行います、出力が無ければOKです")
    results = testmod()
    print("テストが完了しました")
    if results.failed > 0:
        print("テストに失敗しているため、処理を中断します")
        sys.exit(1)
    if results.failed == 0:
        print("0〜99までのトリボナッチ数列を表示します")
        start_time = time.time()
        for i in range(100):
            print(f"{i}: {trib(i)}")
            if time.time() - start_time > 1:
                print("処理時間が1秒を超えたため、強制的に終了します")
                break
