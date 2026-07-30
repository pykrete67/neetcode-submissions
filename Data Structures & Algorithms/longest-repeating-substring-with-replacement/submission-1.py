class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        frequency = {}
        l = 0
        answer = 0

        for index, item in enumerate(s):
            frequency[s[index]] = frequency.get(s[index], 0) + 1
            # answer = max(answer, index-l+1)

            if ((index-l+1) - max(frequency.values()) > k):
                while (index-l+1) - max(frequency.values()) > k:
                    frequency[s[l]] = frequency.get(s[index], 0) - 1
                    # frequency[s[l]] -= 1
                    l += 1
            
            answer = max(answer, index-l+1)

        return answer
