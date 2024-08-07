from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        if n == 2:
            return min(height[0], height[1])
        
        max_area = 0
        i = 0
        j = n-1

        while i < j:
            # print(f"i = {i}; j = {j}")
            # Calculate area
            width = j - i
            height_i = height[i]
            height_j = height[j]
            water_height = min(height_i, height_j)
            area = width * water_height

            # Check if found area is the largest yet
            if area > max_area:
                max_area = area

            if height_i < height_j:
                next_best_i = self.find_next_tallest_line(height, i, j)
                if next_best_i is None:
                    break
                    # raise NotImplementedError("No better i height")
                i = next_best_i
                # i += 1
            elif height_i > height_j:
                next_best_j = self.find_next_tallest_line(height, j, i)
                if next_best_j is None:
                    break
                    # raise NotImplementedError("No better j height")
                j = next_best_j
                # j -= 1
            else:
                # when height_i == height_j
                next_best_i = self.find_next_tallest_line(height, i, j)
                next_best_j = self.find_next_tallest_line(height, j, i)

                if (next_best_i is None) and (next_best_j is None):
                    break
                    # raise NotImplementedError("Neither height improves")
                elif (next_best_i is None):
                    j = next_best_j
                elif (next_best_j is None):
                    i = next_best_i
                elif (next_best_i - i) <= (j - next_best_j):
                    i = next_best_i
                elif (next_best_i - i) > (j - next_best_j):
                    j = next_best_j
                # elif (next_best_i - i) == (j - next_best_j):
                #     raise NotImplementedError("Equal gaps between options")
                else:
                    raise NotImplementedError("Some other crazy case??")

            
            # break

        # print(height[i], height[j])
        # print('max_area', max_area)
        return max_area
    
    def find_next_tallest_line(self, height: List[int], start_index: int, limit_index: int):
        ''' limit_index is exclusive '''
        if start_index < limit_index:
            increment = 1
        elif start_index > limit_index:
            increment = -1
        elif start_index == limit_index:
            raise ValueError("Cannot pass same index for starting and limit positions")
        
        # Find the index of the next tallest line
        start_height = height[start_index]
        for idx in range(start_index, limit_index, increment):
            next_height = height[idx]
            if next_height > start_height:
                return idx
            
        # No better height found
        return None


if __name__ == '__main__':
    sol = Solution()
    print(sol.maxArea([1,8,6,2,5,4,8,3,7]))
    pass