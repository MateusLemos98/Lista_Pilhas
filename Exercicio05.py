def imprimiaInversa(pilha:list):
    pilha_inversa = []

    for i in pilha[::-1]:
        pilha_inversa.append(i)
    return pilha_inversa

x = imprimiaInversa([10, 20, 35, 64, 84, 55, 100])
print(x)