def TPilha(vetor):
    pilha = []

    if len(vetor) == 15:
        for i in range(len(vetor)):
            if vetor[i] % 2 == 0:
                pilha.append(vetor[i])
            else:
                if len(pilha) > 0:
                    pilha.pop()

        for i in range(len(pilha)):
            print(pilha.pop(0))


x = TPilha([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 22, 14, 16])