frutas = ["maçã", "banana", "uva"]
numeros = [1, 2, 3, 4]

#Acessando elementos
print("Primeira fruta:", frutas[0])    
print("Última fruta:", frutas[-1])

#Alterando elementos
frutas[1] = "banana-nanica"
print("Após alterar:", frutas)

#Adicionando elementos
frutas.append("melancia")    #adicionada ao final
frutas.insert(1, "morango")    #adicionada na posição 1
print("Após adicionar:", frutas)

#Removendo elementos
frutas.remove("maçã")         #remove pelo valor
ultima = frutas.pop()       #remove e retorna o último
print("Após remover 'maça' e pop();", frutas, "|Última removida:", ultima)

#Tamanho (quantidade de elementos)
print("Tamanho da lista 'frutas':", len(frutas))

#Fatiamento (slicing)
print("Fatiamento [0:2]:", frutas[0:2]
)

#Verificar se um item está na lista
print("Tem 'morango'?", 'morango' in frutas)

#Iterar sobre lista
for fruta in frutas:
    print("Fruta:", fruta)