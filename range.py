a = [12, 3, 12, 213, 3, 12, 3, 21, 312, 3, 123, 21, 3, 21, 3, 21, 3, 123, 21, 3, 12, 3, 21, 3, 21, 3]
for b in a:
    print(b)
print(a)

for b in range(50):
    b = b + 10
    print(b)
print("================================================================")
for c in range(40, 51):
    print(c)

print("=========================")

con = ["jaime", "lucho", "Luiz", "German", "Mirian", "lucas"]
for i in range(len(con)):
    print(i, con[i])
print("==========================")
print(list(range(10)))
print("======================================================")

for i in range(2, 10):
    for x in range(2, i):
        if i % x == 0:
            print(i, "es igual a ", x, "X", i / x)
            break
    else:
        print(i, "es un mumero primo")

print("======================================================")
multiplicando = 0
for l in range(1, 2):
    for z in range(1, 20):
        multiplicando = multiplicando + 1
        if multiplicando < 10:
            print(z, "X", multiplicando, "=", z * multiplicando)
        elif multiplicando > 10:

            print(z, "+", multiplicando, "=", z + multiplicando)
            multiplicando = 0
            break
    else:
        print("lol")

print("====================================0")
for i in range(2, 10):
    for x in range(2, i):
        if i % x == 0:
            print(i, "es igual a ", x, "X", i / x)
            break
    else:
        print(i, "es un numero primo")

print("=====================================")
for num in range(0, 20):
    if num % 2 == 0:
        print(num, "par")
        continue
    print(num, "impar")

print("==================FUNCIONES========================")


def fibo(n):
    a = 0
    b = 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
        # c = a + b
        # a = b
        # b =c
    print()


fibo(200)

print("========================RESULTADO DE UN FOR EN ARRAYS=========================")
resultado = []
for ja in range(1, 20):
    resultado.append(ja)
    print(resultado)

print("===============================RESULTADO DE UNA FUNCION EN UN ARRAYS")


def fibos(n):
    resul = []
    a = 0
    b = 1
    while a < n:
        resul.append(a)

        a, b = b, a + b
        # c = a + b
        # a = b
        # b =c
    return resul


lol=fibos(200)
print(lol)
