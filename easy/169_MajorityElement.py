class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        count_dict = {}
        for number in nums:
            try:
                count_dict[number] += 1
            except:
                count_dict[number] = 1
        number_max = 0
        number_max_number = 0
        for number in count_dict:
            if count_dict[number] > number_max_number:
                number_max = number
                number_max_number = count_dict[number]
        return number_max

sol = Solution()
nums = [1,2,3,3,3,3,2,1,1,1,2,1,1,1,2,2,2,2,2,2,3]
print(sol.majorityElement(nums))