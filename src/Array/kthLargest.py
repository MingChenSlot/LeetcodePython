__author__ = 'mingchen'

class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {integer}
    # find kth largest
    def findKthLargest(self, nums, k):
        if len(nums) == 0:
            return None
        if len(nums) == 1:
            return nums[0]

        pivot = nums[0]
        j = 1
        for i in range(1, len(nums)):
            if nums[i] > pivot:
                self.switch(i, j, nums)
                j += 1
        self.switch(0, j - 1, nums)

        if j == k:
            return nums[j - 1]
        elif j < k:
            return self.findKthLargest(nums[j:], k - j)
        else:
            return self.findKthLargest(nums[:j - 1], k)

    def switch(self, i, j, nums):
        temp = nums[j]
        nums[j] = nums[i]
        nums[i] = temp

if __name__ == "__main__":
    s = Solution()
    assert s.findKthLargest([-1,2,0], 2) == 0
    assert s.findKthLargest([3,2,1,5,6,4], 2) == 5

