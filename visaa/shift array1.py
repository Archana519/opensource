x = int(input())
arr = list(map(int,input().split()))
r_arr = arr[1:]+[arr[0]]
print(*r_arr)
