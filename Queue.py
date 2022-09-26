# Task 1
from typing import Callable


class Queue:
    __queue: list[str] = []
    __capacity: int

    def __init__(self, capacity):
        if capacity > 0:
            self.__capacity = capacity
        else:
            raise ValueError("capacitance must be greater than 0")

    def is_empty(self) -> bool:
        if len(self.__queue) == 0:
            return True
        else:
            return False

    def is_full(self) -> bool:
        if self.__capacity == len(self.__queue):
            return True
        else:
            return False

    def enqueue(self, char: str):
        if len(char) > 0:
            if not self.is_full():
                self.__queue.append(char[0])
                self.enqueue(char[1:])
            else:
                raise Exception("the queue is full")

    def dequeue(self) -> str:
        if not self.is_empty():
            return self.__queue.pop(0)
        else:
            raise Exception("the queue is empty")

    def show(self) -> str:
        if not self.is_empty():
            show_str = ""
            for num, ch in enumerate(self.__queue):
                show_str += str(num + 1) + " - |" + ch + "|\n"
            return show_str
        else:
            return "the queue is empty"


q = Queue(10)
command_dict = {
    1: (q.is_empty, " - checking the queue for emptiness"),
    2: (q.is_full, " - checking queue for filling"),
    3: (q.enqueue, " - adding an element to the queue"),
    4: (q.dequeue, " - removing an element from the queue"),
    5: (q.show, " - display all elements of the queue on screen")
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
            command_dict[3][0](input("   Enter element> "))
        else:
            print(command_dict[command][0]())
