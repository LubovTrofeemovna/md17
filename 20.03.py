def function1(x):
    if x%7==0:
        return "делится"
    else:
        return "не делится"
y=int(input("введите число"))
print (function1(y))
def function2(x):
    v=200/x
    return v
try:
    y = int(input("введите число]"))
    print(function2(y))
    print('это не число')
except ZeroDivisionError:
    print('нельзя делить на ноль')
except ValueError:
    print('это не число')

def function3(x):
    a,b,c = map(int, y.split("."))
    if a*b == c%100:
        return False
    else:
        return True

y=input('введите дату')
print(function3(y))





