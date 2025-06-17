array = list(map(int , input().split()))
for left in range(len(array)):
    for right in range (left + 1 , len(array)):
        if array[left] > array[right]:
            temp = array[left]
            array[left] = array[right]
            array[right] = temp
print(array)            