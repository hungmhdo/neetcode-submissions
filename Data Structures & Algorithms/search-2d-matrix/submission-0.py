class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # search row

        l = 0
        r = len(matrix) - 1

        while l <= r:
            m = (l + r) // 2

            row = matrix[m]

            if row[0] > target:
                r = m - 1
            elif row[-1] < target:
                l = m + 1
            else:
                l1 = 0
                r1 = len(row) - 1

                while l1 <= r1:
                    m1 = (l1 + r1) // 2
                    if row[m1] > target:
                        r1 = m1 - 1
                    elif row[m1] < target:
                        l1 = m1 + 1
                    else:
                        return True
                
                return False
        
        return False