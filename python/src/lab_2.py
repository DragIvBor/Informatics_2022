import math
a = 1.35
b = 0.98
x = 1.14
print('Задание А:')
# Задание А


def y(x):
    y = (((a * x + b) ** (1 / 3)) / ((math.log(x, math.e)) ** 2))
    return y


if __name__ == '__main__':
    while x < 4.24:
        print(y(x))
        x += 0.62

    # Задание B
    print('Задание B:')
    xlist = [0.35, 1.28, 3.51, 5.21, 4.16]
    xlen = len(xlist)
    for i in range(0, xlen):
        x = xlist[i]
        print(y(x))