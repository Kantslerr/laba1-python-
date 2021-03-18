a = float(input("Введите длину стороны a: "))
b = float(input("Введите длину стороны b: "))
c = float(input("Введите длину стороны c: "))
def f(a,b,c):
    if a + b >= c:
        print("Такой треугольник существует")
    else: print("Треугольник не существует")
f(a,b,c)
