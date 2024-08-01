class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        number_dict = {}
        for number in nums:
            try:
                number_dict[number] += 1
                return True
            except:
                number_dict[number] = 1
        return False