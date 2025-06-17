contact_book = {}
for i in range(3):
    name = input("enter the name=")
    ph_No = int(input())
    contact_book[name] = ph_No
search_name = input("enter the name you need to search =")
if search_name in contact_book:
    print(contact_book[search_name])
else:
    print("contact not found")