class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq = {}
        for st in strs:
            curr_freq = [0] * 26
            for char in st:
                curr_freq[ord(char) - ord("a")] = curr_freq[ord(char) - ord("a")] + 1
            
            freq_key = tuple(curr_freq)

            if freq_key not in freq:
                freq[freq_key] = [st]
            else:
                freq[freq_key].append(st)

        ans = []
        for key in freq:
            ans.append(freq[key])
        
        return ans