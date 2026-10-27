class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        R, C = len(matrix), len(matrix[0])
        r= 0
        c= C-1
        while 0 <= r < R and 0<= c < C:
            print("r:", r,"c:", c)
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] < target:
                r+=1
            else:
                c-=1
        return False
        