class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        rows = len(board)
        cols = len(board[0])

        def backtrack(i,row,col):
            if row < 0 or row >= rows or col < 0 or col >= cols:
                return False

            if board[row][col] != word[i]:
                return False

            if i == len(word) -1:
                return True

            temp = board[row][col]
            board[row][col] = "#"

            for dx, dy in directions:
                next_row = row + dy
                next_col = col + dx
                if backtrack(i+1,next_row,next_col):
                    board[row][col] = temp
                    return True

            board[row][col] = temp
            return False
            
        for row in range(rows):
            for col in range(cols):
                if backtrack(0,row,col):
                    return True
        return False
        