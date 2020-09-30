#
# @lc app=leetcode id=690 lang=python3
#
# [690] Employee Importance
#

# @lc code=start
"""
# Employee info
class Employee:
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution:
    def getImportance(self, employees, query_id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        emap = {e.id: e for e in employees}
        def dfs(eid):
            employee = emap[eid]
            return (employee.importance + sum(dfs(eid) for eid in employee.subordinates))
        return dfs(query_id)

# @lc code=end
if __name__ == '__main__':
    print(Solution().getImportance([[1,2,[2]], [2,3,[]]], 2))

