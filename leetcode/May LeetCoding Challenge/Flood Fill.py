class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        visited = [[False] *len(image[0]) for x in image]
        color = image[sr][sc] #stores the original color
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        def dfs(i, j):
            if i < 0 or i > len(image)-1 or j < 0 or j > len(image[0])-1 or visited[i][j]:
                return
            visited[i][j] = True
            if image[i][j] == color:
                image[i][j] = newColor
                for dir in directions:
                    dfs(i+dir[0], j + dir[1])
        dfs(sr, sc)
        return image