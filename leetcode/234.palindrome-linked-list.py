#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head):
        if head is None or head.next is None:
            return True
        l = []
        p = head
        while p.next:
            l.append(p.val)
            p = p.next
        l.append(p.val)
        return l == l[::-1]

