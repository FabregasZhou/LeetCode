# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        pre_list = ListNode(0)
        sum_list = pre_list
        cin = 0

        while l1 or l2 or cin:
            s = (l1.val if l1 else 0) + (l2.val if l2 else 0) + cin
            if s > 9:
                sum_list.next = ListNode(s - 10)
                cin = 1
            else:
                sum_list.next = ListNode(s)
                cin = 0

            sum_list = sum_list.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return pre_list.next