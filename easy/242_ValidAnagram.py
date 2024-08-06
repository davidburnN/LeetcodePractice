class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict, t_dict = self.get_dict(s), self.get_dict(t)
        return self.get_is_anagram(s_dict, t_dict) if len(s_dict) >= len(t_dict) else self.get_is_anagram(t_dict, s_dict)
        
    def get_dict(self, str: str) -> dict:
        char_dict = {}
        for i in str:
            try:
                char_dict[i] += 1
            except:
                char_dict[i] = 1
        return char_dict
    
    def get_is_anagram(self, dict1, dict2) -> bool:
        is_anagram = True
        for i in dict1:
            try:
                if dict1[i] != dict2[i]:
                    is_anagram = False
            except:
                is_anagram = False
        return is_anagram
    
sol = Solution()
s = 'a'
t = 'ab'
print(sol.isAnagram(s,t))