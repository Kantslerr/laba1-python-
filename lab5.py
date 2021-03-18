a = str(input("Введите строку: "))
def f(a):
    b = 0
    for s in a:
        letter = s.lower()
        if letter == "a" or letter == "e" or\
           letter == "i" or letter == "o" or\
           letter == "u" or letter == "y":
            b += 1
    print("Гласных =",b)
    return b
f(a)    
