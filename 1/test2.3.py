a=''
while a!='stop':
    a=input('введите слово')
    if a != 'stop':
        if 'ф' in a:
            print('Ого! Это редкое слово!')
        else:
         print('Эх, это не очень редкое слово...')