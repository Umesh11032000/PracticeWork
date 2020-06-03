pos = -1


def binarysearch():
    l = 0
    u = len(arr) - 1

    while l <= u:
        mid = (l + u) // 2

        if arr[mid] == n:
            globals()['pos'] = mid
            return True
        else:
            if arr[mid] < n:
                l = mid + 1
            else:
                u = mid - 1

    return False


arr = [10, 20, 30, 40, 50, 60]
n = 60

if binarysearch():
    print("found at index: ", pos)
else:
    print("not found")
