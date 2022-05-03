class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.items:
            return self.items.pop()
        return None

    def is_empty(self):
        return self.items == []
"""*************************************************************************"""

def match_symboles(symbol_str):
    symbol_pairs = {
    '(': ')',
    '[': ']',
    '{': '}'
    }

    openers = symbol_pairs.keys()
    my_stack = Stack()

    index = 0
    while index < len(symbol_str):
        symbol = symbol_str[index]

        if symbol in openers:
            my_stack.push(symbol)
        else: #The symbol is a closer
            #If the stack is already empty, the symbols are not balanced
            if my_stack.is_empty():
                return False

            #If there are still items in the Stacks, check for a mis-match.
            else:
                top_item = my_stack.pop()
                if symbol != symbol_pairs[top_item]:
                    return False

        index += 1

    if my_stack.is_empty():
        return True

    return False # Stack is not empty so symboles were not balanced
"""*************************************************************************"""

print(match_symboles('([{}])'))
print(match_symboles('([{]}])'))
