class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"Node({self.val})"

    def __str__(self):
        return str(self.val)


n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)

# creating linked list
head = n1
n1.next = n2
n2.next = n3
n3.next = n4

node_list = [n1, n2, n3, n4]


head = node_list[0]
temp = head
for i in range(1, len(node_list)):
    j = len(node_list) - i
    if i == j:
        temp.next = node_list[i]
        temp = temp.next
        temp.next = None
    if i >= j:
        temp.next = None
        break

    temp.next = node_list[j]
    temp = temp.next
    temp.next = node_list[i]
    temp = temp.next

print(head)
