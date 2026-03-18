numeros = [7375, 6761, 3512, 4177]
print("Lista original 'numeros':", numeros)

print("Soma dos números:", sum(numeros))

print("Maior número:", max(numeros))

print("Menor número:", min(numeros))

numeros.reverse()
print("Reversa:", numeros)

numeros.sort()
print("Ordenada crescente:", numeros)

numeros.sort(reverse=True)
print("Ordenada decrescente:", numeros)

#List comprehension (exemplo simples)
quadrados = [n * n for n in [1, 2, 3, 4, 5]]
print("Quadrados:", quadrados)