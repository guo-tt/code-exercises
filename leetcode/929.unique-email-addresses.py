#
# @lc app=leetcode id=929 lang=python3
#
# [929] Unique Email Addresses
#
class Solution:
    def numUniqueEmails(self, emails):
        eset = set()
        for email in emails:
            simper = self.simpifyEmail(email)
            eset.add(simper)
        return len(eset)
    
    def simpifyEmail(self, email):
        local, domain = email.split("@")
        local = local.replace('.', '')
        plus_i = local.find('+')
        if plus_i != -1:
            local = local[:plus_i]
        return local + "@" + domain


