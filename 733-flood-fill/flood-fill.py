class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        if not image:
            return 0
         
        rows, cols = len(image), len(image[0])
        visit = set()
        orc = image[sr][sc]

        def bfs(r, c):
            q = collections.deque()
            visit.add((r, c))
            q.append((r, c))

            while q:
                row, col = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if r in range(rows) and c in range(cols) and image[r][c] == orc and (r,c) not in visit:
                        image[r][c] = color
                        q.append((r,c))
                        visit.add((r,c))


        # for r in range(rows):
        #     for c in range(cols):
        #         if image[r][c] == image[sr][sc]:
        #             image[r][c] = color
        #             bfs(r, c)
        bfs(sr, sc)
        image[sr][sc] = color
        return image