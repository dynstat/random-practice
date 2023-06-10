# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"Node({self.val})"

    def __str__(self):
        return str(self.val)


head = None
n1 = ListNode(4)
n2 = ListNode(2)
n3 = ListNode(1)
n4 = ListNode(3)


head = n1
n1.next = n2
n2.next = n3
n3.next = n4
print(head)


def sortList(head):
    list1 = []

    # Traverse
    temp = head
    while temp is not None:
        list1.append(temp.val)
        temp = temp.next

    list1.sort()
    head2 = None
    prev_node = None
    for index, elem in enumerate(list1):
        if index == 0:
            Node0 = ListNode(val=list1[0])
            head2 = Node0

            prev_node = Node0
        else:
            if prev_node:
                curr_node = ListNode(val=elem)
                prev_node.next = curr_node

                prev_node = curr_node
            else:
                break
    print(head2)
    return head2


sortList(head)
