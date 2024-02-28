import random
a=0
d=0
while a<3:
    b=0
    c=0
    b=int(random.randint(-100,100))
    c=int(random.randint(-100, 100))
    z = int(input(f'({b})*({c})='))
    if z==b*c:
        print('молодец! это правильно')
        d=d+1
    else:
        print('ошибка')
        a=a+1
print(f'игра закончена. кол-во правильных ответов - {d}')