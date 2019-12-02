class Solution:
    def spiral_matrix(self, matrix):
        if not matrix:
            return None
        r1, c1 = 0, 0
        r2, c2 = len(matrix), len(matrix[0])
        res = []
        while r1 < r2 and c1 < c2:
            for i in range(c1, c2):
                res.append(matrix[r1][i])    
            r1 += 1
            for i in range(r1, r2):
                res.append(matrix[i][c2 - 1])
            c2 -= 1
            if r1 < r2:
                for i in range(c2 - 1, c1 - 1, - 1):
                    res.append(matrix[r2 - 1][i])
                r2 -= 1
            if c1 < c2:
                for i in range(r2 - 1, r1 - 1, - 1):
                    res.append(matrix[i][c1])
                c1 += 1
        return res

matrix = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

print(Solution().spiral_matrix(matrix))