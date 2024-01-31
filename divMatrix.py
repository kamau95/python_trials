A = [
    [3,0,6,3],
    [1,6,9,11],
    [2,4,8,9]
    ]
divisor = 2

for i in A:
    for element in i:
        result = element / divisor
        print(f"{result:.3f}", end = " ")
    print()
