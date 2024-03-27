def num1():
    x=[2,4,6,7,1]
    y=int(input('введите число'))
    if y in x:
        print (y, x, 'это число есть в списке')
    else:
        print (y, x, 'этого числа нет в списке')
num1()

def num2():
    import random
    x=[]
    for y in range(11):
        x.append(random.randint(0,30))
    print(x)
    for k in x:
        if x.count(k)>1:
            print('число',k, 'повторяется')
        else:
            print('повторяющихся чисел нет')
num2()

def num3():
    x=('понедельник', 'вторник', 'среда', 'четверг' , 'пятница', 'суббота', 'воскресенье')
    y=int(input('введите кол-во выходных'))
    l=x[-y:]
    g = x[:-y]
    print('рабочие:', g, ' ', 'выходные:', l )
num3()


