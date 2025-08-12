class Solution(object):
    def isValidSudoku(self, board):
        for i in range(9):
            line = [x for x in board[i] if x != '.']
            set_line = set(line)
            if len(line) != len(set_line):
                return False
        
        for j in range(9):
            colomn = []
            for i in range(9):
                if board[i][j] != '.':
                    colomn.append(board[i][j])
            set_colomn = set(colomn)
            if len(colomn) != len(set_colomn):
                return False
        
        for box_row in range(0, 9, 3):       # 0, 3, 6
            for box_col in range(0, 9, 3):   # 0, 3, 6
                square = []
                for i in range(3):
                    for j in range(3):
                        val = board[box_row + i][box_col + j]
                        if val != '.':
                            square.append(val)
                if len(square) != len(set(square)):
                    return False
        return True

                
        

        
def main():
    sol = Solution()
    board = [[".",".","4",".",".",".","6","3","."],[".",".",".",".",".",".",".",".","."],["5",".",".",".",".",".",".","9","."],[".",".",".","5","6",".",".",".","."],["4",".","3",".",".",".",".",".","1"],[".",".",".","7",".",".",".",".","."],[".",".",".","5",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."]]


    
    res = sol.isValidSudoku(board)
    print(res)

if __name__ == "__main__":
    main()