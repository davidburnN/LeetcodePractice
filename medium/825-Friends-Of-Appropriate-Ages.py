class Solution:
    def numFriendRequests(self, ages: list[int]) -> int:
        requests = Num_of_Ages(ages).num_of_requests
        return requests

class Num_of_Ages:
    def __init__(self, people):
        print(f'people: {people}')
        self.people = people
        self.ages = self.convert_array(people)
        self.num_of_requests = 0
        self.calculate_requests()

    def convert_array(self, people):
        array = [0] * 120
        for i in people:
            array[i-1] += 1
        return array
    
    def calculate_requests(self):
        for i in range(120):
            for j in range(120-i):
                age_x = i+j+1
                age_y = i+1
                num_of_x = self.ages[i+j]
                num_of_y = self.ages[i]
                if age_y > 0.5*age_x + 7:
                    if j==0:
                        self.num_of_requests += num_of_x*(num_of_x-1)
                        if num_of_x*(num_of_x-1):
                            print(f'x=y, x age: {age_x} num: {num_of_x}, y age: {age_y} num: {num_of_y}, num_of_requests: {num_of_x*(num_of_x-1)}')
                    else:
                        self.num_of_requests += num_of_x*num_of_y
                        if num_of_x*num_of_y:
                            print(f'x=y, x age: {age_x} num: {num_of_x}, y age: {age_y} num: {num_of_y}, num_of_requests: {num_of_x*num_of_y}')
                    



sol = Solution()
testcase1 = [16, 16]
testcase2 = [16, 17, 18]
testcase3 = [20, 30, 100, 110, 120]
testcase4 = [73,106,39,6,26,15,30,100,71,35,46,112,6,60,110]
print(f'testcase1: {sol.numFriendRequests(testcase1)}')
print(f'testcase2: {sol.numFriendRequests(testcase2)}')
print(f'testcase3: {sol.numFriendRequests(testcase3)}')
print(f'testcase4: {sol.numFriendRequests(testcase4)}')
