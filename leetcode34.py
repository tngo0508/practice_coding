class Solution:
    def getRange(self, arr, target):
        first = self.binarySearchIterative(arr, 0, len(arr) - 1, target, True)
        last = self.binarySearchIterative(arr, 0, len(arr) - 1, target, False)
        return [first, last]

    def binarySearch(self, arr, lo, hi, target, findFirst):
        if hi < lo:
            return -1
        mid = lo + (hi - lo) // 2
        if findFirst:
            if mid == 0 or target > arr[mid - 1] and target == arr[mid]:
                return mid
            if target > arr[mid]:
                return self.binarySearch(arr, mid + 1, hi, target, findFirst)
            else:
                return self.binarySearch(arr, lo, mid - 1, target, findFirst)
        else:
            if mid == len(arr) - 1 or target < arr[mid + 1] and target == arr[mid]:
                return mid
            if target < arr[mid]:
                return self.binarySearch(arr, lo, mid - 1, target, findFirst)
            else:
                return self.binarySearch(arr, mid + 1, hi, target, findFirst)

    def binarySearchIterative(self, arr, lo, hi, target, findFirst):
        while True:
            if hi < lo:
                return -1
            mid = lo + (hi - lo) // 2
            if findFirst:
                if (mid == 0 or target > arr[mid - 1]) and target == arr[mid]:
                    return mid
                if target > arr[mid]:
                    lo = mid + 1
                else:
                    hi = mid - 1
            else:
                if (mid == len(arr) - 1 or target < arr[mid + 1]) and target == arr[mid]:
                    return mid
                if target < arr[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1


arr = [5,7,7,8,8,10]
x = 8
print(Solution().getRange(arr, 8))
