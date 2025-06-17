array = list(map(int , input().split())) #10 20 30 40
key = int(input("enter the key="))
left = 0
right = len(array) - 1
while left <= right:
    mid = (left + right) // 2
    if array[mid ] == key:
        print("element found at index")
        break
    if key > array[mid]:
        left = mid + 1
    if key < array[mid]:
        right = mid - 1