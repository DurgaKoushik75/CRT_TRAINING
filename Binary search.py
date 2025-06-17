list1 = list(map(int , input().split()))
list2 = list(map(int , input().split()))
for element in list2:
    key = element
    left = 0
    right = len(list1) - 1
    while left <= right:
        mid = (left + right) //2
        if key == list1[mid]:
            break
        if key < list1[mid]:
            left = mid + 1
        if key > list1[mid]:
            right = mid - 1 
    if key == list1[mid]:
        print("element found at" , mid)
    else:
        print("element not found")
array = list(map(int , input("enter the list:").split()))
key_list = list(map(int , input("enter the keys;").split()))
for index in range(len(key_list)):
        Binary_search(key_list[index])
            
