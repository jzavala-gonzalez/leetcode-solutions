from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort() # this is gonna help so much

        triplets = []

        for i in range(n - 2):
            xi = nums[i]

            if xi > 0:
                break
            elif (i > 0) and (xi == nums[i - 1]):
                continue

            j = i + 1
            k = n - 1

            while j < k:
                xj = nums[j]
                xk = nums[k]
                total = xi + xj + xk

                if total < 0:
                    j += 1
                elif total > 0:
                    k -= 1
                else:
                    triplets.append([xi, xj, xk])
                    while (j + 1 < k) and (nums[j + 1] == xj):
                        j += 1
                    while (k - 1 > j) and (nums[k - 1] == xk):
                        k -= 1
                    j += 1
                    k -= 1
        

        return triplets


if __name__ == '__main__':
    sol = Solution()
    print(sol.threeSum([-1,0,1,2,-1,-4])) # [[-1,-1,2],[-1,0,1]]
    print(sol.threeSum([0,1,1])) # []
    print(sol.threeSum([0,0,0])) # [[0,0,0]]