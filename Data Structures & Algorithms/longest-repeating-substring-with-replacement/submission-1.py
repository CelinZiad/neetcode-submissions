class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        count = {}
        max_length = 0

        for right in range(len(s)):
            if s[right] in count:
                count[s[right]] += 1
            else:
                count[s[right]] = 1

            window_length = right - left + 1
            max_frequency = max(count.values())
            replacement_needed = window_length - max_frequency
            
            while replacement_needed > k:
                count[s[left]] -= 1
                left += 1

                window_length = right - left + 1
                max_frequency = max(count.values())
                replacement_needed = window_length - max_frequency


            max_length = max(max_length, right - left + 1)
        return max_length

        """
        LOGIC:

        add the new character
        ↓
how many characters must I replace?
        ↓
too many?
   /          \
 yes           no
  ↓             ↓
move left    keep window
  ↓             ↓
check again   update max_length 
        """