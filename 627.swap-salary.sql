--
-- @lc app=leetcode id=627 lang=mysql
--
-- [627] Swap Salary
--
# Write your MySQL query statement below
# UPDATE salary SET sex = IF(sex='m', 'f', 'm');
Update salary 
SET sex = CASE sex WHEN 'f' THEN 'm' ELSE 'f' END;

