N = int(input())

if 2 < N < 1000:
    for i in range(1, 11):
        mult = N * i
        print("{} x {} = {}".format(i, N, mult))
if 2 < N < 1000:
    for i in range(1, 11, 1):
        A = i * N
        print("{} x {} = {}".format(i, N, A))
