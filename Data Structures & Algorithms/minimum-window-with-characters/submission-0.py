class Solution:
    def minWindow(self, s: str, t: str) -> str:

        def isValid(w_freq, t_freq):
            for key in t_freq:
                if w_freq.get(key, 0) < t_freq.get(key):
                    return False
            return True
        s_left_idx = 0
        s_right_idx = 0
        # because max length of string is 1000
        shortest = float('inf')
        # add here the frequency of T string
        t_freq = {}
        # keep track of window freq
        w_freq = {}
        left = 0

        for item in t:
            t_freq[item] = t_freq.get(item,0) + 1
        print(f"T Frequency: {t_freq}")

        for right in range(len(s)):
            item = s[right]
            w_freq[item] = w_freq.get(item, 0) + 1
            while isValid(w_freq, t_freq):
                current_shortest = min(shortest,right - left +1)
                if current_shortest < shortest:
                    s_left_idx = left
                    s_right_idx = right
                    shortest = current_shortest
                w_freq[s[left]] -=1
                if w_freq[s[left]] == 0:
                    del w_freq[s[left]]
                left +=1
        if shortest == float('inf'):
            return ""
        return s[s_left_idx:s_right_idx+1]

        