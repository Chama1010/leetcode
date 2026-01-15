#1. Two Sum
#difficulty - easy

class Solution:
    def twoSum(self, nums, target):
        n = len(nums)
        for i in range(n): #d
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]