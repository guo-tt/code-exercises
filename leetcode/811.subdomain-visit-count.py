#
# @lc app=leetcode id=811 lang=python3
#
# [811] Subdomain Visit Count
#

# @lc code=start
import collections

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domain_counts = collections.defaultdict(int)
        for cpdomain in cpdomains:
            times, domains = cpdomain.split()
            times = int(times)
            domain_counts[domains] += times
            while '.' in domains:
                domains = domains[domains.index('.') + 1:]
                domain_counts[domains] += times
        return [str(v) + ' ' + d for d, v in domain_counts.items()]
            

            

        
# @lc code=end

