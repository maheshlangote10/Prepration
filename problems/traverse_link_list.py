

class Node(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

n5 = Node(5)
n4=Node(4,n5)
n3=Node(3,n4)
n2=Node(2,n3)
n1=Node(1,n2)

class LinkList:

    def traverse_list(self, head):
        while head:
            head = head.next

    def add_node_nth_position(self, node,n):
        pass

    def remove_nth_node_from_list(self, n):
        pass


obj = LinkList()
obj.traverse_list(n1)