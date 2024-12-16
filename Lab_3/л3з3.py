try:
    f=open('любой_текст,_ведь_по_заданию_файла_нет.txt').read()
    print(f)
except FileNotFoundError:
    pass
    print('Такого файла нет')