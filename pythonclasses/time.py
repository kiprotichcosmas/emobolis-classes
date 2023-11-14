def adding_numbers(*args):
    total = 0
    for num in args:
        total = total + num
    print(total)
    return total


sum1 = adding_numbers(687, 7656, 7677, 76767, 76776, 76, 7, 67, 6)
sum2 = adding_numbers(798.867, 676, 767)
