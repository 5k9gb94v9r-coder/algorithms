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

def check_h(node):
    if node is None:
        return 0
    hleft = check_h(node.left)
    if hleft == -1:
        return -1

    hright = check_h(node.right)
    if hright == -1:
        return -1

    if abs(hleft - hright) > 1:
        return -1

    return max(hleft, hright) + 1


print("Введите последовательность чисел (последнее число нужно ввести 0):")
root = None
while True:
    n = int(input())
    if n == 0:
        break
    root = insert(root, n)

if check_h(root) != -1:
    print("YES")
else:
    print("NO")