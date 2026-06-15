class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        directions = [(1,0),(0,1),(-1,0),(0,-1)]

        def backtrack(i,row,col):
            if row < 0 or row >= rows or col < 0 or col >= cols:
                return False
            if board[row][col] != word[i]:
                return False

            if i == len(word)-1:
                return True

            temp = board[row][col]
            board[row][col] = '#'

            for dx,dy in directions:
                next_row, next_col = row + dx, col + dy
                if backtrack(i+1,next_row,next_col):
                    board[row][col] = temp
                    return True

            board[row][col] = temp
            return False


        for r in range(rows):
            for c in range(cols):
                if backtrack(0,r,c):
                    return True
        return False



            

                    

        