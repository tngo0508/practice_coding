import collections


def findTime(arr, cooldown):
    cd = collections.defaultdict(lambda: -1)
    i = 0
    j = 1

    while i < len(arr):
        last_seen = cd[arr[i]]
        if last_seen > -1:
            delta = j - last_seen
            if delta >= cooldown:
                cd[arr[i]] = i
                i += 1
                j += 1
            else:
                j += 1
                continue
        else:
            cd[arr[i]] = i
            i += 1
            j += 1
    return j


print(findTime([1, 1, 2, 1], 2))
# 7
