import collections


def generate_skyline(buildings):
    res = []
    pos = collections.OrderedDict()
    for building in buildings:
        for i in range(building[0], building[1] + 1):
            pos[i] = building[2]
    for x, y in pos.items():
        if not res:
            res.append((x, y))
            b = y
        if b != y:
            res.append((x, y))
            b = y
    res.append((x + 1, 0))
    return res

    #            2 2 2
    #            2 2 2
    #        1 1 2 2 2 1 1
    #        1 1 2 2 2 1 1
    #        1 1 2 2 2 1 1
    # pos: 1 2 3 4 5 6 7 8 9
print(generate_skyline([(2, 8, 3), (4, 6, 5)]))
# [(2, 3), (4, 5), (7, 3), (9, 0)]

print(generate_skyline([(2, 4, 1), (3, 3, 2)]))
