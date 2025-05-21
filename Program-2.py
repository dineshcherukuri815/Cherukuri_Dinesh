def odd_series(a):
    num = 1
    for i in range(a):
        print(num, end=", ")
        num += 2
a=int(input("enter a number"))
odd_series(a)
