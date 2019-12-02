import bisect


def grade(score, breakpoints=[60, 70, 80, 90], grades='FDCBA'):
    i = bisect.bisect(breakpoints, score)
    print i
    print breakpoints
    return grades[i]


print ([grade(score) for score in [33, 99, 77, 89, 90, 100]])
