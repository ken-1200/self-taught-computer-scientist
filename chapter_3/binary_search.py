"""文字の探索"""
# 文字コードは、文字と２進数の対応表。
# コンピューターはアルファベットの各文字を7ビットの数値にマッピングしている。
# ほとんどのコンピューターはASCIIコードを8ビットに拡張することで、256文字を表現できるようにしている。
# 100万文字以上の文字を表現できるUnicode文字セットが存在する
# Unicodeの各文字をコンピューター上で実装する方式の1つに、UTF-8文字エンコーディングがある。
# 文字エンコーディングは、文字を数値で表すデジタル表現。
# UTF-8では1文字を最大32ビットでエンコードできる。
# UTF-8はASCIIコードと互換性があるので、ラテン文字のアルファベットを同じビット列で表現している。
# 例えば、A は 01000001
# 二分探索を「文字」の探索に変更する場合は、文字のASCIIコードの値を取得して比較する必要がある。
# ord関数を使って、文字のASCII(アスキー)コードの値を取得
# ord("a") = 97


def binary_search(alphabet_list, word):
    """二分探索 アルファベット順の単語のリストが与えられた時、単語の二分探索を行い、単語がリストに含まれているかどうかを返す関数"""
    _ord_alphabet_list = []
    _ord_word = "".join([str(ord(word[l])) for l in list(range(len(word)))])
    for alphabet in alphabet_list:
        _ord_alphabet_list.append(
            "".join([str(ord(alphabet[l])) for l in list(range(len(alphabet)))])
        )

    first = 0
    last = len(alphabet_list) - 1
    while last >= first:
        mid = (first + last) // 2
        if _ord_alphabet_list[mid] == _ord_word:
            return True
        else:
            if word < alphabet_list[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return False


alphabet_list = [
    "actor",
    "actress",
    "apartment",
    "barley",
    "baseball",
    "call",
    "dirty",
    "eat",
    "fall",
    "go",
    "green",
    "hangover",
    "invite",
    "job",
    "key",
    "last",
    "math",
    "need",
    "office",
    "parents",
    "puppy",
    "read",
    "sad",
    "tomorrow",
    "wallet",
    "yesterday",
]
print(binary_search(alphabet_list, "actor"))


def binary_search_ex(a_list, c):
    """模範解答"""
    first = 0
    last = len(a_list) - 1
    target_code = ord(c)
    while last >= first:
        mid = (first + last) // 2
        if a_list[mid] == c:
            return True
        else:
            if target_code > ord(a_list[mid]):
                first = mid + 1
            else:
                last = mid - 1

    return False


print(binary_search(["a", "b", "c", "d"], "b"))


# --- 書籍の内容 ---
def binary_search_example(a_list: list[int], n: int):
    """二分探索"""
    first = 0
    last = len(a_list) - 1
    while last >= first:
        mid = (first + last) // 2
        if a_list[mid] == n:
            return True
        else:
            if n < a_list[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return False


print(binary_search_example([10, 12, 13, 14, 15, 18, 19], 1))


def binary_search_example_python(an_iterable, target):
    """二分探索 Pythonの組み込み関数を使用した場合"""
    from bisect import bisect_left

    index = bisect_left(an_iterable, target)
    if index <= len(an_iterable) and an_iterable[index] == target:
        return True
    return False


print(binary_search_example_python([10, 12, 13, 14, 15, 18, 19], 10))
