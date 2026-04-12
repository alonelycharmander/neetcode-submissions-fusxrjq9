class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        q = deque()
        q.append((sr, sc))
        prev = image[sr][sc]
        image[sr][sc] = color
        M = len(image)
        N = len(image[0])
        visited = set()
        while q:
            i, j = q.popleft()
            for x, y in [(0,1), (1,0), (0,-1), (-1,0)]:
                dx, dy = x+i, y+j 
                if 0 <= dx < M and 0 <= dy < N and (dx, dy) not in visited and image[dx][dy] == prev:
                    image[dx][dy] = color
                    q.append((dx, dy))
                    visited.add((dx, dy))

        return image

        