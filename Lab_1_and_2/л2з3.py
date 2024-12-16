def is_prime(x):
    m=[]
    for i in range(1,x+1):
        if x%i==0:
            m.append(i)
    if len(m)==2:
        print(True)
    else:
        print(False)
a=int(input())
is_prime(a)