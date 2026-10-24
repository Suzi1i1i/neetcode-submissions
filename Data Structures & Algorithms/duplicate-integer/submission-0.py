class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        sorted_list = sorted(nums)
        l, r = 0, 1
        while l < r and r < len(nums):
            if sorted_list[l] != sorted_list[r]:
                l +=1
                r +=1
            else:
                return True
        return False


        