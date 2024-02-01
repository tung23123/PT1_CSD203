class Bird:
    def __init__(self, type, rate, wing):
        self.type = type
        self.rate = rate
        self.wing = wing
        self.left = None
        self.right = None

class BSTree:
    def __init__(self):
        self.root = None

    def f0(self):
        return "Pham Trung Tung HE187331"

    def insert(self, xType, xRate, xWing):
        if xType[0] == 'B' or xRate > 10:
            return
        else:
            self.root = self._insert(self.root, xType, xRate, xWing)

    def _insert(self, root, xType, xRate, xWing):
        if root is None:
            return Bird(xType, xRate, xWing)
        else:
            if root.rate < xRate:
                root.right = self._insert(root.right, xType, xRate, xWing)
            else:
                root.left = self._insert(root.left, xType, xRate, xWing)
        return root

    def f1(self):
        print("Q1")

        self._inorder(self.root)

    def _inorder(self, root):
        if root:
            self._inorder(root.left)
            print(f"({root.type},{root.rate},{root.wing})", end=" ")
            self._inorder(root.right)

    def f2(self):
        print("\nQ2")
        self._preorder(self.root)

    def _preorder(self, root):
        if root:
            if 4 <= root.wing <= 10:
                print(f"({root.type},{root.rate},{root.wing})", end=" ")
            self._preorder(root.left)
            self._preorder(root.right)

    def f3(self):
        queue = [self.root]
        i = 1
        print("\nQ3")
        while queue:
            node = queue.pop(0)
            if i % 2 != 0:
                print(f"({node.type},{node.rate},{node.wing})", end=" ")
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            i += 1

    def f4(self):
        print("\nQ4")
        self._postorder(self.root)
    def _postorder(self, root):
        if root:
            self._postorder(root.left)
            self._postorder(root.right)
            if root.wing <= 4 and root.rate > 6:
                print(f"({root.type},{root.rate},{root.wing})", end=" ")
def run():
    tree = BSTree()

    print(tree.f0())

    birds = [
        ("A", 5, 9),
        ("E", 2, 5),
        ("D", 8, 6),
        ("F", -6, 7),
        ("X", 4, 5),
        ("Y", 6, -7)
    ]
    for bird in birds:
        tree.insert(*bird)
    tree.f1()

    birds = [
        ("C1", 9, 2),
        ("D", 6, 2),
        ("F", 2, 3),
        ("Z", 8, 1),
        ("H", 1, 7),
        ("I", 3, 9),
        ("Z1", 7, 1),
        ("J", 5, 5),
        ("K", 4, 1)
    ]
    for bird in birds:
        tree.insert(*bird)
    tree.f2()

    birds = [
        ("C", 8, 2),
        ("D", 6, 1),
        ("F", 2, 3),
        ("H", 1, 7),
        ("I", 3, 9),
        ("J", 5, 5),
        ("K", 4, 6),
        ("G", 7, 8),
        ("E", 9, 4)
    ]
    for bird in birds:
        tree.insert(*bird)
    tree.f3()

    birds = [
        ("C", 8, 2),
        ("D", 6, 1),
        ("F", 2, 3),
        ("H", 1, 7),
        ("I", 3, 9),
        ("J", 5, 8),
        ("K", 4, 6),
        ("G", 7, 3),
        ("E", 9, 4)
    ]
    for bird in birds:
        tree.insert(*bird)
    tree.f4()

run()
