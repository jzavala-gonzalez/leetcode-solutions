# Runtime: 65ms beats 88.46%
# Memory: 17.06MB beats 28.20%
from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        max_product = curr_max = curr_min = nums[0]
        for i in range(1, n):
            x = nums[i]
            if x < 0:
                curr_max, curr_min = curr_min, curr_max

            curr_max = max(x, curr_max * x)
            curr_min = min(x, curr_min * x)

            max_product = max(curr_max, max_product)
        
        return max_product
    
if __name__ == '__main__':
    sol = Solution()
    print(sol.maxProduct([-1,-2,-3,0])) # 6