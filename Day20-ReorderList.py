# Definition for singly-linked list.
"""
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…
Given 1->2->3->4, reorder it to 1->4->2->3.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    @staticmethod
    def reorderList(head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head is None:
            return
        high = None
        low = head
        while low:
            low.prev = high
            high = low
            low = low.next
        low = head
        while low != high and low.next != high:
            t = low.next
            low.next = high
            high.next = t

            low = t
            high = high.prev
        high.next = None
