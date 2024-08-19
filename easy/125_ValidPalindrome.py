class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ''
        new_s_l = 0
        for i in s:
            i = self.to_lower(i)
            chrn = ord(i)
            if chrn >= 97 and chrn <= 122:
                new_s += chr(chrn)
                new_s_l += 1
            elif chrn >=48 and chrn <= 57:
                new_s += chr(chrn)
                new_s_l += 1
            
        if new_s_l == 1:
            return True
        for i in range(int(new_s_l/2)):
            try:
                if new_s[i] != new_s[-1-i]:
                    return False
            except:
                return True
        return True
    
    def to_lower(self, cc: str) -> str:
        chrn = ord(cc)
        if chrn >= 65 and chrn <= 90:
            return chr(chrn+32) 
        return cc

sol = Solution()
s = ' '
print(sol.isPalindrome(s))
print(ord(' '))