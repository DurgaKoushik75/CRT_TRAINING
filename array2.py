array = list(map(int , input().split()))
interaction = 1
for i in range(len(array)):
    for j in range(len(array) - interaction):
        if array[j] > array[j + 1]:
            temp = array[j]
            array[j] = array[j + 1]
            array[j + 1] = temp
        interaction += 1    
print(array)            