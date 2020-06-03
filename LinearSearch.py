pos = -1


def search():
    for i in range(len(arr)):
        if arr[i] == n:
            globals()['pos'] = i
            return True

    return False


arr = [10, 5, 9, 6, 20, 15]
n = 9

if search():
    print("found at index: ", pos)
else:
    print("not found")
