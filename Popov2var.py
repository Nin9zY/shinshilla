from math import tan, pi
import time
import functools


def timeoffunction(func):

    @functools.wraps(func)
    def timeneeded(*args, **kwargs):
        strt = time.perf_counter()
        rslt = func(*args, **kwargs)
        thetime = time.perf_counter() - strt
        print(f"Функция: {func.__name__}, Скорость работы: {thetime}\n")
        return rslt

    return timeneeded

#Вычисление площади
@timeoffunction
def polygonarea(length, nmbr):
    nmbr = int(nmbr)
    thearea = (nmbr * length ** 2) / (4 * tan(pi / nmbr))
    print("Площадь многоугольника %.2f " % thearea)

#Сумма чисел
@timeoffunction
def firstsum(n):
    finsum = (n * (n + 1)) / 2
    print("Сумма первых", n ,"положительных чисел = ", finsum)



polygonarea(6, 5)
firstsum(8)