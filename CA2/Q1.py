import sys
import re


class Queue:
    def __init__(self):
        self.queue = []

    def getSize(self):
        return len(self.queue)

    def enqueue(self, value):
        self.queue.append(str(value))

    def dequeue(self):
        if self.isEmpty():
            return None
        return self.queue.pop(0)

    def isEmpty(self):
        if self.getSize() == 0:
            return True
        else:
            return False

    def getInOneLine(self):
        return " ".join(self.queue)


class Stack:
    def __init__(self, size=10):
        self.stack = []
        self.capacity = size

    def isEmpty(self):
        if self.getSize() == 0:
            return True
        else:
            return False

    def push(self, value):
        if self.getSize() == self.getCapacity():
            return None
        self.stack.append(str(value))

    def pop(self):
        if self.isEmpty():
            return None
        return self.stack.pop(self.getSize() - 1)

    def put(self, value):
        self.pop()
        self.push(value)

    def peek(self):
        return self.stack[self.getSize() - 1]

    def expand(self):
        self.capacity *= 2

    def getInOneLine(self):
        return " ".join(self.stack)

    def getSize(self):
        return len(self.stack)

    def getCapacity(self):
        return self.capacity


class Node:
    def __init__(self, val):
        self.data = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def getList(self):
        li = []
        curr_node = self.head
        while (curr_node):
            li.append(str(curr_node.data))
            curr_node = curr_node.next
        return " ".join(li)

    def insertFront(self, new_data):
        new_node = Node(new_data)
        if self.head == None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def insertEnd(self, new_data):
        new_node = Node(new_data)
        if self.head == None:
            self.head = new_node
        else:
            curr_node = self.head
            while (curr_node.next):
                curr_node = curr_node.next
            curr_node.next = new_node

    def reverse(self):
        prev_node = None
        curr_node = self.head
        while (curr_node):
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node
        self.head = prev_node


class Runner:
    dsMap = {'stack': Stack, 'queue': Queue, 'linked_list': LinkedList}
    callRegex = re.compile(r'^(\w+)\.(\w+)\(([\w, ]*)\)$')

    def __init__(self, inputSrc):
        self.input = inputSrc
        self.items = {}

    def run(self):
        for line in self.input:
            line = line.strip()
            action, _, param = line.partition(' ')
            actionMethod = getattr(self, action, None)
            if actionMethod is None:
                return
            actionMethod(param)

    def make(self, params):
        itemType, itemName = params.split()
        self.items[itemName] = self.dsMap[itemType]()

    def call(self, params):
        regexRes = self.callRegex.match(params)
        itemName, funcName, argsList = regexRes.groups()
        args = argsList.split(',') if argsList != '' else []

        method = getattr(self.items[itemName], funcName)
        result = method(*args)
        if result is not None:
            print(result)


def main():
    runner = Runner(sys.stdin)
    runner.run()


if __name__ == "__main__":
    main()
