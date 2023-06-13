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
n5 = ListNode(5)

head = n1
# n1.next = n2
# n2.next = n3
# n3.next = n4
# n4.next = n5


def traverse(temp):
    count = 0

    while temp:
        count += 1
        temp = temp.next
    return count


def removeNthFromEnd(head, n: int):
    temp = head
    # def removeNthFromEnd(head, n: int):
    count = traverse(temp)

    curr = head
    prev = head
    if not head:
        return head
    while count > 0:
        if count == n:
            if prev.next is None:
                head = None
                return head
            else:
                prev.next = prev.next.next
                return head
        prev = curr
        curr = curr.next
        count -= 1


removeNthFromEnd(head, 1)
