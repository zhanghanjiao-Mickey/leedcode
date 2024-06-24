class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        temp_str = []
        result = 1
        for i in range(len(s)):
            if temp_str:
                if s[i] in temp_str:
                    if len(temp_str) > result:
                        result = len(temp_str)
                    temp_str = temp_str[temp_str.index(s[i])+1:]
            temp_str.append(s[i])
            if result < len(temp_str):
                result = len(temp_str)

            # print(temp_str)

        return result

s = "aabaab!bb"
print(Solution().lengthOfLongestSubstring(s))