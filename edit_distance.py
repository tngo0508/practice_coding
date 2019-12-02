def distance(s1, s2):
    # Fill this in.
    # if not s1 and not s2:
    #     return 0
    # if not s1:
    #     return len(s2)
    # if not s2:
    #     return len(s1)
    # if s1[0] == s2[0]:
    #     return distance(s1[1:], s2[1:])
    # insert = 1 + distance(s1, s2[1:])
    # delete = 1 + distance(s1[1:], s2)
    # replace = 1 + distance(s1[1:], s2[1:])
    # print insert, delete, replace
    # return min(insert, replace, delete)

    if len(s1) == 0 or len(s2) == 0:
        return max(len(s1), len(s2))

    return min(distance(s1[1:], s2) + 1,
               distance(s1, s2[1:]) + 1,
               distance(s1[1:], s2[1:]) if s1[0] == s2[0]
               else distance(s1[1:], s2[1:]) + 1)


print distance('biting', 'sitting')
# 2
print distance("prosperity", "properties")
