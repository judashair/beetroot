stack_lifo = []

for i in range(10):
    stack_lifo.append(i)


def get_from_stack(stack, element):
    element_name = 'letter'
    if element.isdigit():
        element_name = 'number'
        element = int(element)
    ware_house_stack = []
    for _ in range(len(stack)):
        now = stack.pop()
        ware_house_stack.append(now)
        if now == element:
            goal = now
            ware_house_stack.pop()
            for _ in range(len(ware_house_stack)):
                stack.append(ware_house_stack.pop())
            return f"Your goal {goal} from stack:\n{stack}"
    raise ValueError(f"There is no {element_name} {element} in stack!\n")


print(get_from_stack(stack_lifo, input("Enter number or letter:\n")))


