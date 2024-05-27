class BST:
    class Node:
        def __init__(self, key, in_indx):
            self.key = key
            self.indx = in_indx
            self.parent = None
            self.left = None
            self.right = None

    def __init__(self, num):
        self.root = None
        self.nodes = [0] * (num + 1)

    def insert(self, key, in_indx):
        new_node = self.Node(key, in_indx)
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
        new_node.parent = p_node
        if key < p_node.key:
            p_node.left = new_node
        else:
            p_node.right = new_node
        self.nodes[p_node.indx] = p_node
        self.nodes[new_node.indx] = new_node

    def getParents(self):
        res = self.nodes[2:]
        res = [n.parent.key for n in res]
        return res
    
    def getLCA(self, a, b):
        node1 = self.nodes[a]
        node2 = self.nodes[b]
        r = self.root
        while r:
            if node1.key < r.key and node2.key < r.key:
                r = r.left
            elif node1.key > r.key and node2.key > r.key:
                r = r.right
            else: break
        return r.indx


def main():
    n = int(input())
    nums = list(map(int, input().split()))[:n]
    a, b = list(map(int, input().split()))[:2]
    tree = BST(n)
    for i in range(n):
        tree.insert(nums[i], i + 1)
    parents = tree.getParents()
    for p in parents:
        print(p, end=' ')
    print()
    print(tree.getLCA(a, b))


if __name__ == "__main__":
    main()