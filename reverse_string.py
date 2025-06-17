string = input()
reverse_string =""
stack = []
for char in string:
    stack.append(char)
while( len(stack) > 0):
    char = stack.pop()
    reverse_string = reverse_string + char
print(reverse_string)    