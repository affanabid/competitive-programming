class Solution:
    def containsDuplicate(self, nums) -> bool:
        dict_ = {}
        for num in nums:
            if num not in dict_:
                dict_[num] = 1
            else:
                dict_[num] += 1
            if dict_[num] > 1:
                return True
        return False