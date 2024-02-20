class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left = 0
        maxfreq = 0
        for r in range(len(s)):
            if s[r] in count:
                count[s[r]] += 1
            else:
                count[s[r]] = 1
            maxfreq = max(maxfreq, count[s[r]])

            if (r - left + 1) - maxfreq > k:
                count[s[left]] -= 1
                left += 1
        return (r - left + 1)
