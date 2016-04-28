print('1 -SUMA')
print('2 -RESTA')
print('3 -MULTIPLICACION')
print('4 -DIVISION')
print('5 -MODULO')
numer=input("ingrese un numero indicando una opcion")
numero=int(numer)
sumador=0
if numero==1:
    print('=============SUMA============')
    numerosuma=input('Ingrese un numero')
    numersuma=int(numerosuma)
    while sumador<12:
        sumador=sumador+1
        print(numersuma,'+',sumador,'=',numersuma+sumador)
elif numero==2:
    print('============RESTA============')
    numerosuma = input('Ingrese un numero')
    numersuma = int(numerosuma)
    while sumador < 12:
        sumador = sumador + 1
        print(numersuma, '-', sumador, '=', numersuma - sumador)
elif numero==3:
    print('=======MULTUPLICACION========')
    numerosuma = input('Ingrese un numero')
    numersuma = int(numerosuma)
    while sumador < 12:
        sumador = sumador + 1
        print(numersuma, 'X', sumador, '=', numersuma * sumador)
elif numero==4:
    print('=========DIVISION============')
    numerosuma = input('Ingrese un numero')
    numersuma = int(numerosuma)
    while sumador < 12:
        sumador = sumador + 1
        print(numersuma, '/', sumador, '=', numersuma /sumador)
elif numero==5:
    print('==========MODULO==============')
    numerosuma = input('Ingrese un numero')
    numersuma = int(numerosuma)
    while sumador < 12:
        sumador = sumador + 1
        print(numersuma, '%', sumador, '=', numersuma % sumador)
else:
    print('******SELECCION INCORRECTA******')


