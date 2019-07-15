class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        s_len = len(s)
        set_len = len([x for x in s])
        max_len = 0
        i = 0
        j = 1
        while j <= set_len:
            s1 = s[i:j]
            long = len(s1)
            if long == len(set([x for x in s1])):
                max_len = max(max_len, long)
                j += 1
                if max_len == set_len:
                    return max_len
            else:
                i += 1
        return max_len
