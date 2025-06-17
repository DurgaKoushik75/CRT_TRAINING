data_base ={}
for i in range(3):
    roll_no = int(input("enter roll number"))
    list = []
    name = input("enter name")
    dept=input("enter dept")
    year= int(input("enter year"))
    list.append(name)
    list.append(dept)
    list.append(year)
    data_base[roll_no]= list
search-roll-number = int(input("enter search roll number"))
if search_roll_number in data base:
    print(data_base[search_roll_number])
else:
    print("student not found")
    
    