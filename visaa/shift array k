def rotate_array(arr, k):
    k = k % len(arr)
    return arr[-k:] + arr[:-k]
N = int(input())
arr = list(map(int, input().split()))
k = int(input())
result = rotate_array(arr, k)
print(" ".join(map(str, result)))
