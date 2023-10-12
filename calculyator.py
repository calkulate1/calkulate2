print('calucale')
a = int(input('введите число '))
b = int(input('введите число '))
c = input('введите символ / +  - * ** ')
if b == 0 and c == '/':
    print('ОШИБКА НА 0 ДЕЛИТЬ НЕЛЬЗЯ')
if c == '+':
    print('a', '+', 'b', '= ', a + b )
if c == '-':
    print('a', '-', 'b', '= ', a - b)
if c == '/' and b != 0:
    print('a', '/', 'b', '= ', a / b )
if c == '*':
    print('a', '*', 'b', '= ', a * b )
if c == '+':
    print('a', '**', 'b', '= ', a ** b )

