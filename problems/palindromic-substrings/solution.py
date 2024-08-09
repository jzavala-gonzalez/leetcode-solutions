class Solution:
    def countSubstrings(self, s: str) -> int:
        total = 0
        n = len(s)
        for i in range(n):
            even_count = self.count_palindromes(s, n, i, i+1)
            odd_count = 1 + self.count_palindromes(s, n, i-1, i+1)

            total += even_count + odd_count
        return total

    def count_palindromes(self, s: str, n: int, left_start: int, right_start: int) -> int:
        tally = 0
        left_index = left_start
        right_index = right_start
        while (left_index >= 0) and (right_index < n) and (s[left_index] == s[right_index]):
            tally += 1
            left_index -= 1
            right_index += 1
        return tally

if __name__ == '__main__':
    sol = Solution()
    print(sol.countSubstrings('abc')) # 3
    print(sol.countSubstrings('aaa')) # 6