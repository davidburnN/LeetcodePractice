class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        len1 = len(nums1)
        len2 = len(nums2)
        totlen = len1+len2
        nums = nums1+nums2
        assert (0<=len1) & (len1<=1000), 'Length of array1 is not available.'
        assert (0<=len2) & (len2<=1000), 'Length of array2 is not available.'
        assert (1<=totlen) & (totlen<=2000), 'Length of array1 and array2 is not available.'
        for i in range(totlen):
            assert (-10**6<=nums[i]) & (nums[i]<=10**6), 'Arrays contain unavailable number.'

        ifDone = 0
        while ifDone<totlen-1:
            ifDone = 0
            for i in range(totlen-1):
                if nums[i]>nums[i+1]:
                    hold = nums[i+1]
                    nums[i+1] = nums[i]
                    nums[i] = hold
                else:
                    ifDone += 1
        
        index = int(totlen/2)
        if totlen%2 == 0:
            median = (nums[index]+nums[index-1])/2
        else:
            median = nums[index]
        print(nums)
        return median

test = Solution()
print(test.findMedianSortedArrays([7,58,100],[37,47,61,55,1,3]))
