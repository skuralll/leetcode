from random import shuffle

array = list(range(30))
shuffle(array)

for end in range(len(array) - 1, -1, -1):
    for i in range(end):
        if array[i] > array[i + 1]:
            temp = array[i]
            array[i] = array[i + 1]
            array[i + 1] = temp

print(array)
