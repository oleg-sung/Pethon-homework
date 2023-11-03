balance_list = [
    '(((([{}]))))',
    '[([])((([[[]]])))]{()}',
    '{{[()]}}'
]
unbalance_list = [
    '}{}',
    '{{[(])]}}',
    '[[{())}]'
]


class Stack(list):
    def isEmpty(self):
        return len(self) == 0

    def push(self, _item):
        self.append(_item)

    def pop_(self):
        if not self.isEmpty():
            _item = self[-1]
            self.__delitem__(-1)
        return _item

    def peek(self):
        if not self.isEmpty():
            return self[-1]

    def size(self):
        return len(self)


def check_balance(seq_):
    balanced_dikt = {
        '(': ')',
        '[': ']',
        '{': '}'
    }
    stack = Stack()
    for item_ in seq_:
        if item_ in balanced_dikt:
            stack.push(item_)
        elif item_ == balanced_dikt.get(stack.peek()):
            stack.pop_()
        else:
            return f'«Несбалансированно»'
    return f'«Сбалансированно»'


if __name__ == '__main__':
    for seq in balance_list + unbalance_list:
        print(f'{seq} - {check_balance(seq)}')
