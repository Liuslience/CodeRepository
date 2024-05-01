class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

head = [1,2,6,3,4,5,6]
val = 6
dummy_node = ListNode()
dummy_node.next = head
# print(dummy_node.next.next)
while dummy_node.next:
    if dummy_node.next.val == val:
        dummy_node.next = dummy_node.next.next
    else:
        dummy_node = dummy_node.next