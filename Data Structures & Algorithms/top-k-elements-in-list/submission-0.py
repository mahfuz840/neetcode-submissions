class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        freq_sorted = dict(sorted(freq.items(), key = lambda x: x[1], reverse = True))

        ans = []
        i = 0
        for key, val in freq_sorted.items():
            ans.append(key)
            i += 1
            if i == k:
                return ans