# Runtime: 70ms beats 67.50%
# Memory: 18.36MB beats 5.92%
from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        max_product = [None for _ in range(n)]
        min_product = [None for _ in range(n)]

        max_product[0] = nums[0]
        min_product[0] = nums[0]
        for i in range(1, n):
            x = nums[i]
            if x >= 0:
                max_product[i] = max(x, max_product[i-1] * x)
                min_product[i] = min(x, min_product[i-1] * x)
            else:
                max_product[i] = max(x, min_product[i-1] * x)
                min_product[i] = min(x, max_product[i-1] * x)
        
        return max(max_product)
    
if __name__ == '__main__':
    sol = Solution()
    print(sol.maxProduct([-1,-2,-3,0])) # 6