from random import randint


def binary_search(l, value) -> bool:
    low = 0
    high = len(l) - 1
    while low <= high:
        mid = (low + high) // 2
        if l[mid] == value:
            return True
        elif l[mid] < value:
            low = mid + 1
        else:
            high = mid - 1
    return False


# ソート済みの配列を用意
arr = list(range(0, 100))
# 適当に間引く
for i in range(0, 50):
    arr.pop(randint(0, len(arr) - 1))

# 結果出力(10回ほどテスト)
for i in range(0, 10):
    num = randint(-50, 50)
    assert binary_search(arr, num) == (num in arr)

print("探索成功")
