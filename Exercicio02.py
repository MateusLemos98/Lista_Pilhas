def pilhasIguais(pilha01:list,pilha02:list):
    if pilha01 == pilha02:
        return True
    else:
        return False

x = pilhasIguais([10, 20, 5, 40, 24],[10, 20, 5, 40, 24])
z = pilhasIguais([1, 2, 3, 4, 5],[5, 4, 3, 2, 1])
print(x)
print(z)