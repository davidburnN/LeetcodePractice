class Solution:
    def countDigits(self, num: int) -> int:
        digit_dict = {}
        num_digit = 0
        for i in range(9):
            digit_dict[f'{i+1}'] = 0
        self.num_str = str(num)
        for i in self.num_str:
            if num%int(i) == 0:
                digit_dict[i] += 1
        for i in digit_dict:
            num_digit += digit_dict[i]
        return num_digit

sol = Solution()
num = 121
print(sol.countDigits(num))