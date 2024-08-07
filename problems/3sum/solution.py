from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort() # this is gonna help so much

        index_hashmap = self.get_index_hashmap(nums)
        # print('index_hashmap', index_hashmap)

        triplets = []
        explored_paths = dict() # k: int, v: dict(k: int, v: Set(int))

        # print('nums', nums)
        for i in range(n-2): # -2 to leave space for j,k
            xi = nums[i]

            if xi not in explored_paths:
                explored_paths[xi] = set()
            elif xi > 0:
                break # can't sum to zero with only positive numbers
            
            for j in range(i + 1, n-1): # -1 because still need k
                xj = nums[j]

                if xj in explored_paths[xi]:
                    continue
                else:
                    explored_paths[xi].add(xj)

                target_xk = -1 * (xi + xj)
                if target_xk not in index_hashmap:
                    continue

                found = False
                for k in index_hashmap[target_xk]:
                    if k > j:
                        xk = nums[k]
                        found = True
                        break
                
                if found:
                    triplets.append([xi, xj, xk])

        return triplets

    def get_index_hashmap(self, nums):
        index_hashmap = dict()
        for (i, x) in enumerate(nums):
            if x not in index_hashmap:
                index_hashmap[x] = list()
            index_hashmap[x].append(i)
        return index_hashmap

if __name__ == '__main__':
    sol = Solution()
    print(sol.threeSum([-1,0,1,2,-1,-4])) # [[-1,-1,2],[-1,0,1]]
    print(sol.threeSum([0,1,1])) # []
    print(sol.threeSum([0,0,0])) # [[0,0,0]]