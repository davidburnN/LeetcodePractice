class Solution:
    def minimumAverageDifference(self, nums: list[int]) -> int:
        NUMS_LEN = len(nums)
        NUMS_SUM = sum(nums)
        sum_left = 0
        num_left = 0
        avg_left = sum_left
        sum_right = NUMS_SUM
        num_right = NUMS_LEN
        avg_right = NUMS_SUM/NUMS_LEN
        min_avg_diff = 10**5
        index = 0
        target_index = 0
        for num in nums:
            sum_left += num
            num_left += 1
            avg_left = int(sum_left/num_left)
            sum_right -= num
            num_right -= 1
            if num_right > 0:
                avg_right = int(sum_right/num_right)
            else:
                avg_right = 0
            avg_diff = abs(avg_left-avg_right)
            if avg_diff < min_avg_diff:
                min_avg_diff = avg_diff
                target_index = index
            print(f'index: {index}, left: {sum_left} avg: {avg_left}, right:{sum_right} avg: {avg_right}')
            index += 1

        return target_index

sol = Solution()
nums = [2,5,3,9,5,3]
nums2 = [0]
nums3 = [0,1,0,1,0,1]
print(sol.minimumAverageDifference(nums3))