a = int(input("введите номер места "))
if a >= 37:
    print("боковое")
else:
    print("купе")
if a % 2 == 1: print("нижнее")
else:
    print("верхнее")