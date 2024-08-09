from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        solutions_cache = dict()
        n = len(s)

        def mini_word_break(i):
            if i in solutions_cache:
                return solutions_cache[i]
            if i >= n:
                return True
            
            for j in range(i+1, n+1):
                if (s[i:j] in word_set) and mini_word_break(j):
                    solutions_cache[i] = True
                    return True
                
            solutions_cache[i] = False
            return False
        
        return mini_word_break(0)

if __name__ == '__main__':
    sol = Solution()
    print(sol.wordBreak('leetcode', ['leet', 'code'])) # True
    print(sol.wordBreak("applepenapple", ["apple","pen"])) # True
    print(sol.wordBreak("catsandog", ["cats","dog","sand","and","cat"])) # False
    print(sol.wordBreak("goalspecial", ["go","goal","goals","special"])) # True


