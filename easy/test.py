class Solution(object):
    def twoSum(nums, target):
        i = 0
        j = len(nums) - 1
        
        while (nums[i] + nums[j] != target):
            if (nums[i] + nums[j] > target):
                j = j - 1
            else:
                i = i + 1
                
        return [i, j]

# ans = Solution()
# ans2 = ans.twoSum([1,2,3],4)
# print(ans)
# print(ans2)
print(Solution.twoSum([1,2,3],4))