def witnesses(heights):
    witness_count = 0
    tallest = 0
    for height in heights[::-1]:
        if height > tallest:
            tallest = height
            witness_count += 1

    return witness_count

print(witnesses([3, 6, 3, 4, 1]))
# 3