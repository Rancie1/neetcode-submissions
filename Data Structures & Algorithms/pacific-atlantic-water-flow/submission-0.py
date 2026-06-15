class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        


        ROWS = len(heights)
        COLS = len(heights[0])
        pac, atl = set(), set()
        directions = [(0,1),(1,0),(-1,0),(0,-1)]


        def dfs(row,col,seen,prevHeight):
            if row < 0 or row >= ROWS or col < 0 or col >= COLS or (row,col) in seen or heights[row][col] < prevHeight:
                return

            seen.add((row,col))
            dfs(row+1,col,seen,heights[row][col])
            dfs(row-1,col,seen,heights[row][col])
            dfs(row,col+1,seen,heights[row][col])
            dfs(row,col-1,seen,heights[row][col])


        for c in range(COLS):
            dfs(0,c,pac,heights[0][c])
            dfs(ROWS-1,c,atl,heights[ROWS-1][c])

        for r in range(ROWS):
            dfs(r,0,pac,heights[r][0])
            dfs(r,COLS-1,atl,heights[r][COLS-1])

        ans = []

        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in atl and (r,c) in pac:
                    ans.append((r,c))

        return ans

        

        


            



        