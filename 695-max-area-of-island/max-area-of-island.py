class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visited = set()
        count = 0

        def bfs(r, c):
            q = collections.deque()
            q.append((r, c))
            visited.add((r, c))

            curr_count = 1

            while q:
                rol, col = q.popleft()
                directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

                for dr, dc in directions:
                    r, c = rol + dr, col + dc
                    if r in range(rows) and c in range(cols) and grid[r][c] == 1 and (r,c) not in visited:
                        curr_count += 1
                        q.append((r, c))
                        visited.add((r, c))
            return curr_count



        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    curr_count = bfs(r, c)
                    count = max(count, curr_count)
        return count
