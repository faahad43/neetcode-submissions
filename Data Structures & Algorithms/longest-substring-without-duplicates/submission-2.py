class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        left = 0
        lastseen = {}
        for right in range(len(s)):
            item = s[right]
            # if this is a new character
            if item not in lastseen:
                print(f"iter: {item}")
                lastseen[item] = right
                print(f"the dic: {lastseen}")
                longest = max(longest ,right - left +1)
                print(f"the longest: {longest}")
            
            # if already present character
            # uptill now all the character in the string are same as s
            # so now we have to move the left till the index where this repeated is gone
            # mean 1 index next to first occurence of repeated character
            # zxycxp -- now reaching at x you have to move the left to y

            else:
                print(f"iter else: {item}")
                left = max(left, lastseen[item] + 1 )
                print(f"the left else: {left}")
                lastseen[item] = right
                print(f"the dic else: {lastseen}")
                longest = max(longest ,right - left +1)
                print(f"the longest else: {longest}")

        return longest
                


        