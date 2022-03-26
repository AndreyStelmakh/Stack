

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def is_empty(self):
        if self.top is None:
            return True
        else:
            return False

    def push(self, data):
        self.top = StackNode(data, self.top)
        self.size += 1

    def pop(self):
        if not self.is_empty():
            result = self.top.data
            self.top = self.top.next_node
            self.size -= 1
            return result
        else:
            raise IndexError

    def peek(self):
        if not self.is_empty():
            return self.top.data
        else:
            raise IndexError

    def size(self):
        return self.size


class StackNode:
    def __init__(self, data, next_node):
        self.data = data
        self.next_node = next_node


def is_bracket_balanced(string):
    stack = Stack()

    opens = '([{'
    closes = ')]}'
    for symbol in string:
        if symbol in opens:
            stack.push(symbol)
        elif symbol in closes:
            if stack.is_empty():
                return 'Несбалансированно'
            stack_bracket = stack.peek()
            if (symbol == ')' and stack_bracket == '(') or \
                (symbol == ']' and stack_bracket == '[') or \
                (symbol == '}' and stack_bracket == '{'):
                stack.pop()
            else:
                return 'Несбалансированно'

    return 'Сбалансированно'


if __name__ == '__main__':

    print(is_bracket_balanced('(((([{}]))))'))
    print(is_bracket_balanced('[([])((([[[]]])))]{()}'))
    print(is_bracket_balanced('{{[()]}}'))
    print(is_bracket_balanced('}{}'))
    print(is_bracket_balanced('{{[(])]}}'))
    print(is_bracket_balanced('[[{())}]'))
