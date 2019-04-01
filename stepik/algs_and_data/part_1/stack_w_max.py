class Stack:
    def __init__(self):
        self._stk = []

    def __ensure_non_empty(self):
        if len(self._stk) == 0:
            raise IndexError("Empty stack")

    def is_empty(self):
        return len(self._stk) == 0

    def push(self, v):
        self._stk.append(v)
    
    def peek(self):
        self.__ensure_non_empty()
        return self._stk[-1]
    
    def pop(self):
        self.__ensure_non_empty()
        return self._stk.pop()

    def size(self):
        return len(self._stk)




if __name__ == "__main__":
    comands = []
    steps = int(input())
    s = Stack()
    for i in range(0,steps):
        c = input()
        if c.startswith('push'):
            s.push(c.split(" ")[1])
        elif c == "pop":
            print(s.pop())
        else:
            print(f'WTF: unknown command: {c}')
    
    