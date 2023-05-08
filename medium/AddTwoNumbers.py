class ListNode:
    def __init__(self, val = 0, next = None, list = None):
        self.list = list
        self.len = len(list)

    def __repr__(self):
        n = 0
        for i in range(self.len):
            n += self.list[i]*10**(i)
        return f'{n}'

    def checkConstraints(self):
        assert self.len < 101 and self.len > 0, 'the number of nodes should be in the range [1, 100]'
        if self.len > 1:
            assert self.list[-1]!=0, 'first node should not be 0' 
        else:
            for i in self.list:
                assert i >= 0 and i <= 9, 'the value of each node should be between 0 and 9'
    
    
class Solution:
    def addTwoNumbers(self, l1, l2):
        if l1.len > l2.len:
            for i in range(l1.len):
                if l1.list[i]+l2.lsit[i]:
                    pass

l1 = ListNode([0,0,3])
l1.checkConstraints()

l2 = ListNode([5,5,5,2])
l2.checkConstraints()

solution = Solution().addTwoNumbers(l1, l2)
print(solution)