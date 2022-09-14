#! /Users/sehuang/opt/anaconda3/bin/python3.8
import numpy as np

class Solution:
	def twoSum(self, nums, target):
		assert len(nums)>=2 and len(nums)<=10**4, "length of the array is too short, which should be between 2 and 10000"
		assert max(nums)<=10**9 and min(nums)>=-10**9, "numbers in the array should be between -10^9 and 10^9"
		assert target>=-10**9 and target<=10**9, 'target should be between -10^9 and 10^9'
		nums = np.array(nums)
		subtraction = target-nums
		for i in range(len(subtraction)):
			if subtraction[i] in nums:
				j = np.where(nums == subtraction[i])[0][0]
				if i == j:
					continue
				else:
					break
		return [i, j]
sol = Solution()

nums = [3,2,4]
target = 6
ans = sol.twoSum(nums, target)

print(f'nums = {nums}, target = {target}\noutput: {ans}')
