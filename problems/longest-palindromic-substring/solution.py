class Solution:
    def longestPalindrome(self, s: str) -> str:
        # s is at least 1 char long
        n = len(s) # >= 1

        max_length = 0
        longest_palindrome = ''
        for i in range(n):
            even_palindrome = self.iterate_palindrome(s, n, i, i+1)
            odd_palindrome  = self.iterate_palindrome(s, n, i-1, i+1)

            if len(odd_palindrome) >= len(even_palindrome):
                palindrome = odd_palindrome
            else:
                palindrome = even_palindrome

            length = len(palindrome)
            if length > max_length:
                max_length = length
                longest_palindrome = palindrome

            # print('s', s)
            # print('even_palindrome', even_palindrome)
            # print('odd_palindrome', odd_palindrome)
            # break

        return longest_palindrome

    def iterate_palindrome(self, s: str, n: int, left_start: int, right_start: int) -> str:
        ''' Breaks and returns whatever palindrome it found.
         left_start and right_start are inclusive
        '''

        left_index = left_start
        right_index = right_start
        while (left_index >= 0) and (right_index < n) and (s[left_index] == s[right_index]):
            left_index -= 1
            right_index += 1
        
        return s[left_index+1:right_index]

if __name__ == '__main__':
    sol = Solution()
    # print(sol.iterate_palindrome('babab', 5, 0, 2))
    print(sol.longestPalindrome('babad')) # 'bab' or 'aba'
    print(sol.longestPalindrome('cbbd')) # 'bb'