array = list(map(int , input().split())) #10 20 30 40
key = int(input("enter the key"))
for index in range(len(array)):
    if array[index] == key:
        break
    if array[index] == key:
        print[" key found at " , index+1]
    else:
        print("key not found")