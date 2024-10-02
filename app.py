'''
Crie um programa que possa:
- Inserir o nome de um usuário em uma lista
- Exibir a lista de nomes
- Ordenar os nomes
- Alterar o nome na lista
- Excluir um nome da lista
- Sair do programa
O programa deverá exibir um menu e o usuário irá escolher a opção desejada do menu.
Ao terminar, envie para o GitHub e poste o link do repositório no Classroom.
'''

# Lista de carros
carros = ["Gol", "Linea", "Mercedes", "Palio", "Santana", "Corvette", "Civic", "Fit"]

# Exibir a lista original
for i in range(len(carros)):
    print(f"índice {i}: {carros[i]}")

# usuário deve informa o índice que deseja alterar
try:
    indice = int(input("Digite o índice do carro que deseja alterar ou deletar: "))
    confirmacao = input(f"Informe a modificação que deseja realizar em {carros[indice]}: Digite '1' para fazer uma alteração ou '2' para excluir {carros[indice]} da lista.")

    if confirmacao == "1":
        novo_carro = input("Informe o novo carro: ")
        carros[indice] = novo_carro
    elif confirmacao == "2":
        del(carros[indice])
        print("carro deletado com sucesso.")
    else:
        ...
except Exception as e:
    print(f"Não foi possível executar comando. {e}")
finally:
    # nova lista
    for i in range(len(carros)):
        print(f"Índice {i}: {carros[i]}.")