# Task 2
from typing import Callable


class PriorityQueue:
    __priority_queue: dict[int, list[str]] = {}
    __capacity: int
    __tail: int = 0

    def __init__(self, capacity):
        if capacity > 0:
            self.__capacity = capacity
        else:
            raise ValueError("capacitance must be greater than 0")

    def is_empty(self) -> bool:
        if len(self.__priority_queue) == 0:
            return True
        else:
            return False

    def is_full(self) -> bool:
        if self.__capacity == self.__tail:
            return True
        else:
            return False

    def insert_with_priority(self, char: str, priority: int):
        if type(char) == str and type(priority) == int:
            if len(char) == 1:
                if not self.is_full():
                    if priority in self.__priority_queue.keys():
                        self.__priority_queue[priority].append(char)
                    else:
                        self.__priority_queue[priority] = [char]
                    self.__tail += 1
                else:
                    raise Exception("the queue is full")
            else:
                raise ValueError("char must be one character")
        else:
            raise TypeError

    def pull_highest_priority_element(self) -> str:
        if not self.is_empty():
            max_priority = max(self.__priority_queue.keys())
            popped_elem = self.__priority_queue[max_priority].pop(0)
            self.__tail -= 1
            if len(self.__priority_queue[max_priority]) == 0:
                del self.__priority_queue[max_priority]
            return popped_elem
        else:
            raise Exception("the queue is empty")

    def peek(self) -> str:
        if not self.is_empty():
            max_priority = max(self.__priority_queue.keys())
            return self.__priority_queue[max_priority][0]
        else:
            raise Exception("the queue is empty")

    def show(self) -> str:
        if not self.is_empty():
            show_str = ""
            for num, (p, ch) in enumerate(self.__priority_queue.items()):
                show_str += str(num + 1) + " - {" + str(p) + "}|" + str(ch) + "|\n"
            return show_str
        else:
            return "the queue is empty"


q = PriorityQueue(5)
command_dict = {
    1: (q.is_empty, " - checking the queue for emptiness"),
    2: (q.is_full, " - checking queue for filling"),
    3: (q.insert_with_priority, " - adding an element with priority to the queue"),
    4: (q.pull_highest_priority_element, " - removing the highest priority element from the queue"),
    5: (q.peek, " - return the highest priority element"),
    6: (q.show, " - display all elements of the queue on screen")
}


def show_menu(menu_dict: dict[int, tuple[Callable, str]]) -> str:
    menu_str = "Menu\n\t0 - quit\n"
    for k, v in menu_dict.items():
        menu_str += "\t" + str(k) + v[1] + "\n"
    return menu_str


while True:
    print(show_menu(command_dict))
    command = int(input("Enter command> "))
    if command in command_dict or command == 0:
        if command == 0:
            print("shutdown...")
            break
        elif command == 3:
            command_dict[3][0](input("   Enter element> "), int(input("   Enter priority> ")))
        else:
            print(command_dict[command][0]())
