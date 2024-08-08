from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashmap = set(nums)

        max_length = 0
        for x in hashmap:
            if x-1 in hashmap:
                continue

            length = 1
            x_next = x+1
            while x_next in hashmap:
                length += 1
                x_next += 1
            
            if length > max_length:
                max_length = length

        return max_length
    
if __name__ == '__main__':
    sol = Solution()
    print(sol.longestConsecutive([100, 4, 200, 1,3,2])) # 4
    print(sol.longestConsecutive([0,3,7,2,5,8,4,6,0,1])) # 9