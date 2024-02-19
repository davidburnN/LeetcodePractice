class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> list[int]:
        array = [0] * num_people
        i = 0
        while i < candies:
            array[i%num_people] += i + 1 
            i += 1
            candies -= i
        array[i%num_people] += candies
            
        return array
    
sol = Solution()
candies = 20
num_people = 3
print(sol.distributeCandies(candies, num_people))