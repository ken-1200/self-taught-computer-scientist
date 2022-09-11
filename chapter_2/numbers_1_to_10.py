def numbers_1_to_10(n):
    """再帰的アルゴリズム 1-10までの数字を出力"""
    if n == 0:
        return
    print(n)
    return numbers_1_to_10(n - 1)


numbers_1_to_10(10)


def print_r(n):
    """模範解答"""
    if n == 0:
        return
    print(n)
    n -= 1
    print_r(n)


print_r(10)
