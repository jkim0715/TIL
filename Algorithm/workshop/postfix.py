class ArrayStack:

    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]

prec = {
    '*': 3, '/': 3,
    '+': 2, '-': 2,
    '(': 1
}

def solution(S):
    opStack = ArrayStack()

    answer = ''
    for c in S:
        if c not in prec:
            answer += c
        elif c == '(':
            opStack.push(c)
        elif c == ')':
            for _ in range(opStack.size()):
                if opStack.peek() != '('
                    answer += opStack.pop()
                else:
                    opStack.pop()
        else:
            while not opStack.isEmpty():
                if prec[opStack.peek() >= prec[c]]:
                    answer += opStack.pop()
                else:
                    break
            opStack.push(c)
    
    while not opStack.isEmpty():
        answer += opStack.pop()
        
    return answer