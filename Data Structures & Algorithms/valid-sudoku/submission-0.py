class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowCheck = [set() for _ in range(9)] 
        colCheck = [set() for _ in range(9)]
        threeCheck = [[set() for _ in range(3)] for _ in range(9)]

        for i in range(9):
            r = board[i]
            for j in range(9):
                e = r[j]
                if e == '.':
                    continue

                x = i // 3
                y = j // 3

                # Row check
                if e in rowCheck[i]:
                    return False
                else:
                    rowCheck[i].add(e)

                # Col check
                if e in colCheck[j]:
                    return False
                else:
                    colCheck[j].add(e)
                
                # 3x3 check
                if e in threeCheck[x][y]:
                    return False
                else:
                    threeCheck[x][y].add(e)

        return True