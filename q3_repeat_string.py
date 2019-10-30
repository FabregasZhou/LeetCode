class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        sub_begin = 0
        s_dict = {}
        for i in range(len(s)):
            if (s_dict.get(s[i]) != None) and (s_dict.get(s[i]) >= sub_begin):
                sub_len = i - sub_begin

                if sub_len > max_len:
                    max_len = sub_len

                sub_begin = s_dict[s[i]] + 1

            s_dict[s[i]] = i

        if len(s) - sub_begin > max_len:
            max_len = len(s) - sub_begin

        return max_len