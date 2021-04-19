class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def init_tree():
    root = Node('A')

    node_b = Node('B')
    root.left = node_b

    node_c = Node('C')
    root.right = node_c

    node_d = Node('D')
    node_b.left = node_d

    node_e = Node('E')
    node_b.right = node_e

    node_f = Node('F')
    node_c.left = node_f

    node_g = Node('G')
    node_c.right = node_g

    return root


# 전위순회
def preorder_traverse(node):
    if node is None:
        return
    print(node.data, end="->")
    preorder_traverse(node.left)
    preorder_traverse(node.right)


# 중위순회
def inorder_traverse(node):
    if node is None:
        return
    inorder_traverse(node.left)
    print(node.data, end="->")
    inorder_traverse(node.right)


# 후위순회
def postorder_traverse(node):
    if node is None:
        return
    inorder_traverse(node.left)
    inorder_traverse(node.right)
    print(node.data, end="->")


# 단계순회
def levelorder_traverse(node):
    levelq = []
    levelq.append(node)

    while len(levelq) != 0:
        # visit
        visit_node = levelq.pop(0)
        print(visit_node.data, end="->")
        # child put
        if visit_node.left is not None:
            levelq.append(visit_node.left)
        if visit_node.right is not None:
            levelq.append(visit_node.right)

if __name__ == "__main__":
    tree = init_tree()
    preorder_traverse(tree)
    print()
    inorder_traverse(tree)
    print()
    postorder_traverse(tree)
    print()
    levelorder_traverse(tree)

