a = int(input("Введите число a: "))
b = int(input("Введите число b: "))
c = int(input("Введите число c: "))
def f(a,b,c):
    D = b**2-4*a*c
    x1 = (-b + D**0.5)/(2*a)
    x2 = (-b - D**0.5)/(2*a)
    if D < 0:
        print("Решения нет")
    elif a*x1**2+b*x1+c==0 and a*x2**2+b*x2+c==0:
        if x1 == x2:
            print("Ответ: ",x1)
        else: print("Ответ: ",x1,x2)
    elif a*x1**2+b*x1+c==0:
        print("Ответ: ",x1)
    elif a*x2**2+b*x2+c==0:
        print("Ответ: ",x2)
    else: print("Решения нет")
f(a,b,c)
