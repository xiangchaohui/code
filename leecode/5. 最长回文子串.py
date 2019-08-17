class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n <= 1:
            return s
        max_len = 0
        max_str = s[0]
        for i in range(1, n):
            if i == 1:
                if s[0] == s[1]:
                    max_len == 1
                    max_str = s[:2]
                continue
            str_len = min(i - 1, n - i)
            str1 = s[:i - 1][::-1]
            str2 = s[i:]

            compar = [str1[i] == str2[i] for i in range(str_len)]
            for compar_index in range(str_len):
                if not compar[compar_index]:
                    compar_index -= 1
                    break

            compar_len = (compar_index + 1) * 2 + 1

            if compar_len > max_len and compar_len>1:
                max_len = compar_len
                max_str = s[i - 1 - compar_index - 1: i - 1 + compar_index + 1 + 1]

            ###
            str_len = min(i, n - i)
            str1 = s[:i][::-1]
            str2 = s[i:]

            compar = [str1[i] == str2[i] for i in range(str_len)]

            for compar_index in range(str_len):
                if not compar[compar_index]:
                    compar_index -= 1
                    break

            compar_len = (compar_index + 1) * 2

            if compar_len > max_len and compar_len>1:
                max_len = compar_len
                max_str = s[i - 1 - compar_index: i - 1 + compar_index + 1 + 1]
        return max_str