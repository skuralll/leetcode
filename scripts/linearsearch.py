from random import randint


def linear_search(l, value) -> bool:
    for i in l:
        if i == value:
            return True
    return False


# ソート済みの配列を用意
arr = list(range(0, 100))
# 適当に間引く
for i in range(0, 50):
    arr.pop(randint(0, len(arr) - 1))

# 結果出力(10回ほどテスト)
for i in range(0, 10):
    num = randint(-50, 50)
    assert linear_search(arr, num) == (num in arr)

print("探索成功")
