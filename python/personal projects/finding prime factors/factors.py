num = int(input("enter number"))

factor = 2
while num > 1:
    if num % factor == 0:
        print(factor)
        num = num/factor
    else:
        factor += 1
