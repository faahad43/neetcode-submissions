class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        freq = {}
        left = 0
        
        for right in range(len(s)):
            
            item=s[right]
            freq[item] = freq.get(item,0) + 1
            
            while True:
                window = right - left + 1
                most_frequent_value = max(freq.values())
                invalid = window - most_frequent_value > k

                if not invalid:
                    break
                    
                freq[s[left]] -=1
                if freq[s[left]] == 0:
                    del freq[s[left]]
                left +=1
            longest = max(longest, window)

        return longest
        