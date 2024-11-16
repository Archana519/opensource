X = int(input())
d_p_10 = 0.90 * X
d_f_100 = X - 100
f_p = min(d_p_10, d_f_100)
print(int(f_p))
