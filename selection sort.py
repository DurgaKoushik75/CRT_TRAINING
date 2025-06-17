array = list(map(int , input().split()))
for i in range(len(array)):
    mini = array[i]
    index = i
    for j in range(i + 1, len(array)):
        if array[j] < mini:
            mini = array[j]
            index = j
    temp = array[i]
    array[i] = mini
    array[index] = temp
print(array)    