
'''
Exercício de lógica
Criando um programa que adicione e Busque por pessoas utilizando Listas.

'''
lista = ['Lucas', 'Pedro', 'Jorge']

while True:
    print('\n============ OPÇÕES ============')
    print("""
            (1). Adicionar Pessoa;
            (2). Buscar Pessoa;
            (3). Remover Pessoa.
                                """)

    op = int(input('Escolha uma das opções acima:\n'))

    if op == 1:
        pessoa =input("Insira o nome a ser adicionado:\n")
        lista.append(pessoa)

    elif op == 2:
        pessoa = input('Insire o nome da pessoa a ser verificada no sistema:\n')
        if pessoa in lista:
            print(f"Sim,o {pessoa} está na lista!")
        else:
            print(f"Não,o {pessoa} está na lista.")

    elif op == 3:
        pessoa =  input("Insira o nome para ser removido da lista:\n")
        if pessoa in lista:
            lista.remove(pessoa)  # variavel.remove() = faz que voce remove algo da lista na posição
            print("Esta pessoa foi removida da lista com sucesso!")
        else:
            print("Esta pessoa não se encontra no sistema da lista.")
    else:
        print("Opção inválida!")

    print(lista)

  



