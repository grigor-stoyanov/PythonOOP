from typing import List


class Stack:
    def __init__(self, data=None):
        if not data:
            self.data: List[str] = []
        self.data = data

    def push(self, element) -> None:
        if isinstance(element, str):
            self.data.append(element)

    def pop(self) -> str:
        return self.data.pop()

    def top(self) -> str:
        return self.data[-1]

    def is_empty(self) -> bool:
        return not any(self.data)

    def __str__(self):
        return f'[{", ".join([ele for ele in reversed(self.data)])}]'


my_stack = Stack(['a', 'b'])
print(my_stack)
