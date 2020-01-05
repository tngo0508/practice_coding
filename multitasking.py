def findTime(arr, cooldown):
    lastPos = {}
    pos = 0
    for num in arr:
        if num in lastPos:
            if pos - lastPos[num] <= cooldown:
                # Add cooldown
                pos = cooldown + lastPos[num] + 1
        lastPos[num] = pos
        pos = pos + 1
    return pos


print(findTime([1, 1, 2, 1], 2))
# 7
