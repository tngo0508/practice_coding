def dutch_flag_partition(arr, idx):
    pivot = arr[idx]
    smaller, equal, larger = 0, 0, len(arr) - 1
    while equal <= larger:
        if arr[equal] < pivot:
            arr[equal], arr[smaller] = arr[smaller], arr[equal]
            equal += 1
            smaller += 1
        elif arr[equal] == pivot:
            equal += 1
        else:
            arr[equal], arr[larger] = arr[larger], arr[equal]
            larger -= 1

    return arr


print(dutch_flag_partition([0, 1, 2, 0, 2, 1, 1], 2))


def invariant1(arr, val1, val2, val3):
    smaller, equal, larger = 0, 0, len(arr) - 1
    while equal <= larger:
        if arr[equal] == val1:
            arr[equal], arr[smaller] = arr[smaller], arr[equal]
            equal += 1
            smaller += 1
        elif arr[equal] == val2:
            equal += 1
        elif arr[equal] == val3:
            arr[equal], arr[larger] = arr[larger], arr[equal]
            larger -= 1

    return arr


print(invariant1([0, 1, 2, 0, 2, 1, 1], 0, 1, 2))


def invariant2(arr, val1, val2, val3, val4):
    smaller, equal, larger = 0, 0, len(arr) - 1
    fourth = larger - 1
    while equal <= larger:
        if arr[equal] == val1:
            arr[equal], arr[smaller] = arr[smaller], arr[equal]
            equal += 1
            smaller += 1
        elif arr[equal] == val2:
            equal += 1
        elif arr[equal] == val3:
            arr[equal], arr[larger] = arr[larger], arr[equal]
            larger -= 1
        elif arr[equal] == val4:
            arr[equal], arr[fourth] = arr[fourth], arr[equal]
            fourth -= 1
    return arr


print(invariant2([0, 1, 3, 2, 0, 3, 2, 3, 1, 1, 3, 3], 0, 1, 2, 3))
