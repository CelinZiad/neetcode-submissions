class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = set()
        left = 0
        max_length = 0

        for right in range(len(s)):
            while s[right] in substring:
                substring.remove(s[left])
                left+=1
            
            substring.add(s[right])
            max_length = max(max_length, right - left+1)
        return max_length
        """
        substring = []
        first = s[0]
        substring.append(first)
        for i in range (1,len(s)-1):
            second = s[i]
            substring.append(second)
            if substring[0]==substring[len(substring)-1]:
                substring.pop(0)
        return len(substring)
        """


