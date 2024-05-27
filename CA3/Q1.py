import sys
import re


INVALID_INDEX = 'invalid index'
OUT_OF_RANGE_INDEX = 'out of range index'
EMPTY = 'empty'


class MinHeap:
    class Node:
        def __init__(self, value):
            self.val = value

    def __init__(self):
        self.heap = []
    
    def get_left(self, parent):
        return 2 * parent + 1
    
    def get_right(self, parent):
        return 2 * parent + 2
    
    def check_exception(self, index):
        if not isinstance(index, int):
            raise Exception('invalid index')
        if index < 0 or index >= len(self.heap):
            raise Exception('out of range index')
        if not len(self.heap):
            raise Exception('empty')
        
    def bubble_up(self, index):
        self.check_exception(index)
        indexOfP = (index - 1) // 2
        while indexOfP >= 0:
            if self.heap[indexOfP].val > self.heap[index].val:
                self.heap[indexOfP], self.heap[index] = self.heap[index], self.heap[indexOfP]
            else: break
            index = indexOfP
            indexOfP = (index - 1) // 2

    def bubble_down(self, index):
        self.check_exception(index)
        left = self.get_left(index)
        right = self.get_right(index)
        if index >= len(self.heap) // 2: return
        less = index
        if left < len(self.heap) and self.heap[less].val > self.heap[left].val:
            less = left
        if right < len(self.heap) and self.heap[less].val > self.heap[right].val:
            less = right
        if less != index:
            self.heap[less].val,self.heap[index].val = self.heap[index].val,self.heap[less].val
            self.bubble_down(less)

    def heap_push(self, value):
        new_node = self.Node(value)
        self.heap.append(new_node)
        self.bubble_up(len(self.heap)-1)

    def heap_pop(self):
        if not len(self.heap):
            raise Exception('empty')
        popped = self.heap[0].val
        self.heap[0].val = self.heap[-1].val
        self.heap.pop()
        if len(self.heap): 
            self.bubble_down(0)
        return popped

    def find_min_child(self, index):
        self.check_exception(index)
        left = self.get_left(index)
        right = self.get_right(index)
        if left < len(self.heap) and right < len(self.heap):
            if self.heap[left].val < self.heap[right].val:
                return left
            else: return right
        elif left < len(self.heap) and right > len(self.heap):
            return left

    def heapify(self, *args):
        for val in args:
            self.heap_push(val)


class HuffmanTree:
    class Node:
        def __init__(self, l, f, left = None, right = None):
            self.letter = l
            self.freq = f
            self.left = left
            self.right = right
            self.dir = ""

    def __init__(self):
        self.letters = []
        self.freqs = []
        self.head = None
        self.encoded = {}

    def set_letters(self, *args):
        self.letters = args
        self.encoded = {i:None for i in self.letters}

    def set_repetitions(self, *args):
        self.freqs = args

    def build_huffman_tree(self):
        nodes = list(zip(self.letters, self.freqs))
        nodes = [self.Node(i, j) for i, j in nodes]
        nodes.sort(key = lambda x : (x.freq, x.letter), reverse = True)
        

        while len(nodes) > 1:
            nodes.sort(key = lambda x : (x.freq), reverse = True)
            l = nodes.pop()
            r = nodes.pop()
            l.dir = "0"
            r.dir = "1"
            new_node= self.Node(None, l.freq + r.freq, l, r)
            nodes = [new_node] + nodes
            self.head = new_node
        self.encoding(node = self.head)

    def encoding(self, node, huff_code = ""):
        c = huff_code + node.dir
        if node.left:
            self.encoding(node.left, c)
        if node.right:
            self.encoding(node.right, c)
        if not node.left and not node.right:
            self.encoded[node.letter] = c

    def get_huffman_code_cost(self):
        cost = 0
        i = 0
        for l in self.encoded:
            cost += len(self.encoded[l]) * self.freqs[i]
            i += 1
        return cost

    def text_encoding(self, text):
        l = {}
        for i in text:
            l[i] = l[i] + 1 if i in l else 1
        self.letters = list(l.keys())
        self.freqs = list(l.values())
        self.encoded = {i:None for i in self.letters}
        self.build_huffman_tree()


class Bst:
    class Node:
        def __init__(self, key):
            self.key = key
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    def insert(self, key):
        new_node = self.Node(key)
        if not self.root:
            self.root = new_node
            return
        tmp = self.root
        p_node = None
        while tmp != None:
            p_node = tmp
            if key < tmp.key:
                tmp = tmp.left
            else: tmp = tmp.right
        if key < p_node.key:
            p_node.left = new_node
        else:
            p_node.right = new_node

    def inorder(self):
        tmp = self.root
        if not tmp: return
        res = []
        stack = []
        while True:
            while tmp != None:
                stack.append(tmp)
                tmp = tmp.left
            if not len(stack): break
            popped = stack.pop()
            res.append(popped.key)
            tmp = popped.right
        return " ".join(map(str, res))

class Runner:
    dsMap = {'min_heap': MinHeap, 'bst': Bst, 'huffman_tree': HuffmanTree}
    callRegex = re.compile(r'^(\w+)\.(\w+)\(([\w, \-"\']*)\)$')

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

        args = [x.strip() for x in argsList.split(',')] if argsList != '' else []
        args = [x[1:-1] if x[0] in ('"', "'") else int(x) for x in args]

        method = getattr(self.items[itemName], funcName)
        try:
            result = method(*args)
        except Exception as ex:
            print(ex)
        else:
            if result is not None:
                print(result)


def main():
    runner = Runner(sys.stdin)
    runner.run()


if __name__ == "__main__":
    main()
