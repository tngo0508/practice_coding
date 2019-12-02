class Solution(object):
    def pushDominoes(self, dominoes):
        N = len(dominoes)
        force = [0] * N

        # Populate forces going from left to right
        f = 0
        for i in range(N):
            if dominoes[i] == 'R':
                f = N
            elif dominoes[i] == 'L':
                f = 0
            else:
                f = max(f-1, 0)
            force[i] += f

        # Populate forces going from right to left
        f = 0
        for i in range(N-1, -1, -1):
            if dominoes[i] == 'L':
                f = N
            elif dominoes[i] == 'R':
                f = 0
            else:
                f = max(f-1, 0)
            force[i] -= f

        result = ''
        for f in force:
            if f == 0:
                result += '.'
            elif f > 0:
                result += 'R'
            else:
                result += 'L'
        return result


print(Solution().pushDominoes('..R...L..R.'))
# ..RR.LL..RR
print(Solution().pushDominoes('..RRRL..RL.'))
# ..RRRL..RL.