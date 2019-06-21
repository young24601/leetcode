import bisect

def closest_pair(arr1, arr2, x):
    print(arr1[bisect.bisect(arr1, x)-1])

    print(arr2[bisect.bisect(arr2, x)-1])

    return 0


arr1 = [1, 4, 5, 7]
arr2 = [10, 20, 30, 40]
x = 32
closest_pair(arr1, arr2, x)


arr1 = [1, 4, 5, 7]
arr2 = [10, 20, 30, 40]
x = 50
closest_pair(arr1, arr2, x)
