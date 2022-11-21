def maiorElemento(pilha):
  maiorEle = pilha[0]
  for i in range(len(pilha)):
    if pilha[i] > maiorEle:
      maiorEle = pilha[i]
  return maiorEle

p = maiorElemento([0, 2, 9, 6, 15])
print(p)

