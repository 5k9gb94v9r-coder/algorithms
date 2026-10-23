class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def insert(root, value):
    if root is None:
        return Node(value)
    if value < root.value:
        root.left = insert(root.left, value)
    elif value > root.value:
        root.right = insert(root.right, value)
    return root


def inorder(node, result):
    if node is None:
        return
    inorder(node.left, result)

    has_left = node.left is not None
    has_right = node.right is not None
    if has_left != has_right:
        result.append(node.value)

    inorder(node.right, result)


print("Введите последовательность чисел (последнее число нужно ввести 0):")
root = None
while True:
    n = int(input())
    if n == 0:
        break
    root = insert(root, n)

result = []
inorder(root, result)
print(*result)