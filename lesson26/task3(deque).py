queue_fifo = []

for i in range(10):
    queue_fifo.append(i)


def get_from_stack(queue, element):
    element_name = 'letter'
    if element.isdigit():
        element_name = 'number'
        element = int(element)
    ware_house_queue = []
    for _ in range(len(queue)):
        now = queue.pop(0)
        if now == element:
            goal = now
            queue = ware_house_queue + queue
            return f"Your goal {goal} from queue:\n{queue}"
        if now != element:
            ware_house_queue.append(now)
    raise ValueError(f"There is no {element_name} {element} in queue!\n")


print(get_from_stack(queue_fifo, input("Enter number or letter:\n")))
