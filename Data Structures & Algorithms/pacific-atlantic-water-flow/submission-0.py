class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # Create two sets to keep track of which points are able 
        # to reach which ocean

        # Then the points that are in both sets are appeneded to answer

        ROWS, COLS = len(heights), len(heights[0])

        pacificOcean, atlanticOcean = set(), set()

        res = []

        # Pacific Ocean is the TOP and RIGHT edges
        # Atlantic is the RIGHT and BOTTOM edges

        # DFS function to traverse the matrix
        def dfs(r, c, visited, prevHeight):
            if ((r,c) in visited or r < 0 or c < 0 or r == ROWS or c == COLS or heights[r][c] < prevHeight):
                return
            
            visited.add((r,c))
            dfs(r + 1, c, visited, heights[r][c])
            dfs(r - 1, c, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])

        # Find all points starting from TOP row that reach Pacific Ocean
        # And all points from BOTTOM row that reach Atlantic
        for c in range(COLS):
            dfs(0, c, pacificOcean, heights[0][c])
            dfs(ROWS - 1, c, atlanticOcean, heights[ROWS - 1][c])
        
        # Find all points starting from RIGHT col that reach Pacifc
        # And all points starting from Left col that reach Atlantic
        for r in range(ROWS):
            dfs(r, 0, pacificOcean, heights[r][0])
            dfs(r, COLS - 1, atlanticOcean, heights[r][COLS - 1])

        # Check each points to see which sets they are in
        for r in range(ROWS):
            for c in range(COLS):
                if ((r,c) in pacificOcean and (r,c) in atlanticOcean):
                    res.append((r,c))
        
        return res
            