def factorial(n):
    """再帰的アルゴリズム 階乗"""
    if n == 0:
        return 1
    return n * factorial(n - 1)


print(factorial(3))

# [return n * factorial(n - 1) n = 3
# return n * factorial(n - 1) n = 2
# return n * factorial(n - 1) n = 1
# 1]

# 結果から解答を辿る
# return n * factorial(n - 1) n = 1
# 1 * 1 = 1
# return n * factorial(n - 1) n = 2
# 2 * 1 = 2
# return n * factorial(n - 1) n = 3
# 3 * 2 = 6
