class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0 

        rows = len(grid)
        cols = len(grid[0])
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        islands = 0

        def bfs(r,c):
            q = deque()
            grid[r][c] = "0"
            q.append((r,c))
            while q:
                row,col = q.popleft()
                for dx, dy in directions:
                    next_row = row + dx
                    next_col = col + dy
                    if next_row < 0 or next_row >= rows or next_col < 0 or next_col >= cols or grid[next_row][next_col] == "0":
                        continue

                    grid[next_row][next_col] = "0"
                    q.append((next_row,next_col))

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    islands += 1
                    bfs(row,col)
        return islands



        