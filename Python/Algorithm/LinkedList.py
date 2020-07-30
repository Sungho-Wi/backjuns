class Node:
    def __init__(self, data, next_=None):
        self.data = data
        self.next = next_


# A -> B -> C -> D 로 된 linked list 생성
def init_list():
    node_a = Node('A')
    node_b = Node('B')
    node_c = Node('C')
    node_d = Node('D')
    node_a.next = node_b
    node_b.next = node_c
    node_c.next = node_d
    return node_a


def print_list(linked_list):
    while linked_list:
        print(linked_list.data, end=' ')
        linked_list = linked_list.next


def insert_node(node, data, index):
    new_node = Node(data)

    if index == 0:
        new_node.next = node
        return new_node

    pre_node = node
    curr_node = node

    for i in range(index):
        if curr_node is not None:
            pre_node = curr_node
            curr_node = curr_node.next

    pre_node.next = new_node
    new_node.next = curr_node
    return node


def delete_node(node, data):
    if node.data == data:  # 첫번째 노드를 삭제할 경우 pre_node 가 없으므로 linkedList 시작을 두번째 노드로 설정
        node = node.next
        return node

    pre_node = node
    curr_node = node.next

    while curr_node:
        if curr_node.data == data:
            pre_node.next = curr_node.next
            break

        pre_node = curr_node
        curr_node = curr_node.next

    return node


linkedList = init_list()
print_list(linkedList)

print()  # 줄넘김
print('INSERT 노드 추가')

insertedNode = insert_node(linkedList, "INSERT", 0)
print_list(insertedNode)

print()
print('INSERT 노드 삭제')

deletedNode = delete_node(linkedList, "INSERT")
print_list(deletedNode)
