from random import shuffle


def quicksort(seq):
    if len(seq) <= 1:
        return seq
    pivot = seq[0]
    left = []
    right = []
    for x in range(1, len(seq)):
        if seq[x] <= pivot:
            left.append(seq[x])
        else:
            right.append(seq[x])
    left = quicksort(left)
    right = quicksort(right)
    foo = [pivot]
    return left + foo + right


array = list(range(30))
shuffle(array)

print(quicksort(array))
