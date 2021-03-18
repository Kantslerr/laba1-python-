x = float(input("Введите первое число: "))
y = float(input("Введите второе число: "))
z = float(input("Введите третье число: "))
if x <= y and x <= z:
    print (x)
elif y <= x and y <= z:
    print(y)
else: print(z)    
