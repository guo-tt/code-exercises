#
# @lc app=leetcode id=203 lang=python3
#
# [203] Remove Linked List Elements
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head, val):
        new_head = pre = ListNode(0)
        pre.next = head # sudo head 
        while head:
            if head.val == val:
                pre.next = head.next
            else:
                pre = pre.next
            head = head.next
        return new_head.next

