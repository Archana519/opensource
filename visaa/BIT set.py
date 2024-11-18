x = int(input())
y = int(input())
z = 1 << (y-1)
if x & z:
  print("true")
else:
  print("false")
