print('Введите число')
a=int(input())
if a>0:
    for i in range(1,a+1): print(i)
if a==0 or a < 0:
    print('Число должно быть больше нуля')