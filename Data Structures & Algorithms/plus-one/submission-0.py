class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        max_idx = len(digits) - 1
        print(max_idx)
        def rec(idx):
            print("rec:", idx)
            if digits[idx] == 9:                    
                digits[idx] = 0
                if idx == 0:
                    digits.insert(0, 1)
                    return
                else:
                    rec(idx-1)
            elif digits[idx] != 9:
                digits[idx] += 1
                return
        rec(max_idx)
        return digits