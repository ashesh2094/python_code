# Find a pair with maximum product in array of Integers


def maxProduct(list, n):
    if (n < 2):
        print("No pairs exists")
        return
    a = list[0]
    b = list[1]
    for i in range(0, n):
        for j in range(i + 1, n):
            if (list[i] * list[j] > a * b):
                a = list[i]
                b = list[j]

    print("Max product pair is [", a, ",", b,"]")

list = [1, 2, 3 , 4 , 5, 6]
n = len(list)
maxProduct(list, n)
