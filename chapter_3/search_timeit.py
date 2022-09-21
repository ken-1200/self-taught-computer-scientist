import bisect
import random
import timeit

data = list(range(1_000))
random.shuffle(data)

# 線形探索
print(timeit.timeit(lambda: 1 in data))

# ソートするコストは高い
print(timeit.timeit(lambda: sorted(data)))

# 何度も探索する場合はソートしておく
datasorted = sorted(data)

# 二分探索は線形探索より速い
print(timeit.timeit(lambda: bisect.bisect(datasorted, 1)))

# set へ変換するコストは高い
print(timeit.timeit(lambda: set(data)))

# 何度も探索する場合は set に変換しておく
dataset = set(data)

# ハッシュ探索は二分探索より速い
print(timeit.timeit(lambda: 1 in dataset))
