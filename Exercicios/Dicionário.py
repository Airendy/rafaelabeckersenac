aluna = {"id": 1, "nome": "Rafaela", "nota": 9.2}
pessoa = {"nome": "Ana", "idade": 25}

#Acessar valores por chave
print("Nome da pessoa:", pessoa["nome"])

#Adicionar e alterar chaves/valores
pessoa["cidade"] = "Florianópolis"  
pessoa["idade"] = 26
print("Pessoa atualizada:", pessoa)

#Remover chave
removido = pessoa.pop("idade")
print("Valor removido (idade):", removido)
print("Após pop('idade'):", pessoa)

#Tamanho
print("Quantidade de chaves em 'aluna':", len(aluna))

#Listar chaves, valores e itens(pares)
print("Chaves de 'aluna':", list(aluna.keys()))
print("Valores de 'aluna':", list(aluna.values()))
print("Itens de 'aluna':", list(aluna.items()))
