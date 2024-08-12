from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)

        i, j = 0, n-1
        while nums[i] > nums[j]:
            k = (i + j) // 2
            if i == k:
                i += 1
            elif nums[i] > nums[k]:
                j = k
            else:
                i = k
        return nums[i]
        