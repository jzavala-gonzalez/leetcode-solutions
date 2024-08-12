# 36ms beats 92.09%, 16.96MB beats 30.33%
# TODO: Review una solucion mas elegante luego
from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        i, j = 0, n-1
        while i < j-1:
            # if nums[i] == target or nums[j] == target:
            #     break

            k = (i + j) // 2
            xi, xj, xk = nums[i], nums[j], nums[k]
            left_ascending = xi < xk
            right_ascending = xk < xj
            print('xi, xj =', xi, xj)
            if (xi <= target <= xk) or ((not left_ascending) and ((xi <= target) or (target <= xk))): # Left
                j = k
                pass
            elif (xk <= target <= xj) or ((not right_ascending) and ((xk <= target) or (target <= xj))): # Right
                i = k
                pass
            else:
                return -1

        if nums[i] == target:
            return i
        elif nums[j] == target:
            return j
        else:
            return -1