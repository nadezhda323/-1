def sum_nums(x,y):
    try:
        a=int(x)+int(y)
        return a
    except:
        print("Введите только числа!")
        return 0
def sub_nums(x,y):
    a=x-y
    return a
def sab_nums(x,y):
    a=x*y
    return a
def sam_nums(x,y):
    try:
        a=int(x)/int(y)
        return a
    except ZeroDivisionError:
        print("На ноль делить нельзя!")
    except:
        print("Введите только числа!")
        return 0
print(sam_nums(5,3))


