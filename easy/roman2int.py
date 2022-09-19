# from tabnanny import check


class Solution:
    def romanToInt(self, s: str) -> int:
        if (len(s)<1):
            print(f"No insert value.")
            return 0
        elif len(s)>15:
            print(f"{s} is oversiced.")
            return 0
        
        #check characters
        roman_character = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
            }
        list_not_roman_character = []
        for i in s:
            if (i in roman_character)==0:
                list_not_roman_character.append(i)
        if len(list_not_roman_character)>0:
            print(f"{list_not_roman_character} are not roman characters.")
            return 0
        
        #calculating 

        
s = "I"
Solution().romanToInt(s)

