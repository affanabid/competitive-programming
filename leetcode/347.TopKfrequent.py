from collections import Counter

class Solution:
    def topKFrequent(self, nums, k: int):
        dic = {}
        
        for num in nums:
            if num in dic:
                dic[num] += 1
            else:
                dic[num] = 1
        
        sorted_dic = sorted(dic.items(), key=lambda x:x[1], reverse=True)
        
        freq = []
        for num, occ in sorted_dic[:k]:
            freq.append(num)
        
        return freq
            
