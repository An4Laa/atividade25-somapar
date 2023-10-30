numero = []

for i in range(0, 6) :
    inserirnumero = int(input("Digite o número: "))
    if inserirnumero % 2 == 0:
        numero.append(inserirnumero)

soma = sum(numero)
print(soma)