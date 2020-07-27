class Solution:

    def longestPalindrome(self, s: str) -> str:

        def get_max_length(s, idx_left, idx_right):
            while (s[idx_left] == s[idx_right]):
                if idx_left - 1 < 0 or idx_right + 1 > len(s) - 1:
                    return idx_left, idx_right
                else:
                    idx_left -= 1
                    idx_right += 1

            return idx_left + 1, idx_right - 1

        idx_left = 0
        idx_right = 0

        for i in range(len(s)):
            left, right = get_max_length(s, i, i)
            if right - left > idx_right - idx_left:
                idx_left = left
                idx_right = right

            if i < len(s) - 1:
                left, right = get_max_length(s, i, i + 1)
                if right - left > idx_right - idx_left:
                    idx_left = left
                    idx_right = right

        return s[idx_left:idx_right + 1]