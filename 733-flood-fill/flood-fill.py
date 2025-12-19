class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        if not image:
            return 0

        rows, cols = len(image), len(image[0])

        visited = set()
        

        def bfs(r, c):
            q = collections.deque()
            q.append((r, c))
            visited.add((r, c))

            while q:
                rol, col = q.pop()

                directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

                for dr, dc in directions:
                    r, c = rol + dr, col + dc

                    if r in range(rows) and c in range(cols) and image[sr][sc] == image[r][c] and (r, c) not in visited:
                        image[r][c] = color
                        q.append((r, c))
                        visited.add((r, c))
            

        bfs(sr, sc)
        image[sr][sc] = color
        return image

    

        