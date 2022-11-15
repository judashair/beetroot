from stack import Stack

stack_1 = Stack()
input_str = input("Enter some charachetes:\n")
for i in input_str:
    stack_1.push(i)
print(stack_1)
