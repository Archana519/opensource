a,b,c,d = map(int, input().split())
if a+b>=d or a+c>=d or b+c>=d:
    print("YES")
else:
    print("NO")
