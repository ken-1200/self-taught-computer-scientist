def merge_sort(a_list):
    """マージソート

    リストを要素数が1つになるまで、サブリストに分割していく。
    最も効率的なソートアルゴリズムの一つで、Pythonの組み込みソートアルゴリズムにも使われている（時間計算量はO(n log n)）

    Pythonには list の sort メソッドと、任意のイテラブルをソートできる sorted 組み込み関数がある。
    これらのソート関数は、Timsort という、マージソートと挿入ソートを足し合わせたソートアルゴリズム（ハイブリッドソートアルゴリズム）を使っている。
    """
    if len(a_list) > 1:
        mid = len(a_list) // 2
        left = a_list[:mid]
        right = a_list[mid:]

        merge_sort(left)
        merge_sort(right)

        left_i = 0
        right_i = 0
        alist_i = 0
        # マージ処理
        while left_i < len(left) and right_i < len(right):
            if left[left_i] <= right[right_i]:
                a_list[alist_i] = left[left_i]
                left_i += 1
            else:
                a_list[alist_i] = right[right_i]
                right_i += 1
            alist_i += 1

        while left_i < len(left):
            a_list[alist_i] = left[left_i]
            left_i += 1
            alist_i += 1

        while right_i < len(right):
            a_list[alist_i] = right[right_i]
            right_i += 1
            alist_i += 1

    # merged
    return a_list


a_list = [6, 3, 9, 2, 4, 1]
print(merge_sort(a_list))


"""
- 処理の動き

※下記の処理の中で、自信を呼び出す際に渡した値と受け取った値は同じものを指す。
再帰中に受けとった値を変更すると、渡した値も変更されることを理解しておく必要がある。

a_list = [6, 3, 9, 2] の場合

スタート
    -> 再帰(merge_sort(渡す))
        -> 再帰(merge_sort(渡す)) -> merged
            -> ソート(受け取った値は上位処理内の値を変更している) -> merged
                -> 渡した値が変更されている
                    -> ソート(left と right を統合する)
                        -> merged

ソート（統合）の処理の流れ -- マージ処理
各要素の 0 番目同士で値の大小を比較して、小さいものをリターンするリストの要素に追加している
M
L [3, 6]
R [2, 9]
merged
[2, 3, 6, 9]

-> 再帰(merge_sort(渡す)) -> ソート(受け取った値は上位処理内の値を変更している) -> ストップ
この処理が要素が1つにならない限り呼ばれ続ける
2つのリストの中でソートする処理から3つ、4つと処理が行われている
"""
