numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(squared)


print((lambda m,n : m + n) (9,34))

print("---------------------")

listA = [3,8,7]
listB = [0,5,1]
addedList = list(map(lambda a,b : a+b, listA, listB))
print(addedList)

print("-----------------------")

trixA = [
        [20,12,16],
        [11,21,40],
        [98,34,17]
        ]
trixB = [
        [67,12,31],
        [12,54,33],
        [80,99,88]
        ]
addedTrix = list(map(lambda A,B : A + B, trixA, trixB))
print(addedTrix)
