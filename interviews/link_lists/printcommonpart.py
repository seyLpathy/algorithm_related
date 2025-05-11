# 给定两个有序链表的头指针head1 和head2，打印两个链表的公共部分。
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def printcommonpart(head1, head2):
    print("common part:\n")
    while head1 and head2:
        if head1.value < head2.value:
            head1 = head1.next
        elif head1.value > head2.value:
            head2 = head2.next
        else:
            print(head1.value)
            head1 = head1.next
            head2 = head2.next


def removemid(head):
    if not head or not head.next:
        return head
    if head.next.next:
        return head.next
    fast = head.next.next
    slow = head
    while slow.next and slow.next.next:
        fast = fast.next.next
        slow = slow.next
    slow.next = slow.next.next
    return head


def reverse_single_link_list(head):
    pre = None
    while head:
        next = head.next
        head.next = pre
        pre = head
        head = next
    return pre


def reverse_double_link_list(head):
    prev = None
    next = None
    while head:
        next = head.next
        head.next = prev
        head.last = next
        prev = head
        head = next
    return prev