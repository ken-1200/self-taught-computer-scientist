def bubble_sort(a_list):
    """バブルソート データ量が少ない時には十分に使えるアルゴリズム（時間計算量はO(n**2)）"""
    loop_size = len(a_list) - 1
    for i in range(loop_size):
        no_swaps = True
        for j in range(loop_size - i):
            if a_list[j] > a_list[j + 1]:
                a_list[j], a_list[j + 1] = a_list[j + 1], a_list[j]
                no_swaps = False
        if no_swaps:
            return a_list
    return a_list


a_list = [32, 1, 9, 6]
print(bubble_sort(a_list))
