class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        islands = 0

        ROWS = len(grid)
        COLS = len(grid[0])

        def dfs(row,col):
            if row < 0 or row >= ROWS or col < 0 or col >= COLS or grid[row][col] == "0":
                return

            grid[row][col] = "0"
            for dx, dy in directions:
                dfs(row+dx,col+dy)

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == "1":
                    islands += 1
                    dfs(row,col)
        return islands
                


        