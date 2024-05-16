import os

restaurantes = [{"nome": "Cantina toscana" , "categoria": "Italiana", "ativo": True},
                {"nome": "Sushi da Praça", "categoria": "Japonesa", "ativo": False},
                {"nome": "Churrascaria Gaúcha", "categoria": "Brasileira", "ativo": True},
                {"nome": "Padaria Pão Doce", "categoria": "Padaria", "ativo": True}]


def exibir_nome_do_programa():
    print("""
    █▀▀ ▄▀█ █▀▄ ▄▀█ █▀ ▀█▀ █▀█ █▀█ █▀   █▀▄ █▀▀   █▀█ █▀▀ █▀ ▀█▀ ▄▀█ █░█ █▀█ ▄▀█ █▄░█ ▀█▀ █▀▀ █▀   █▀█ █▄░█ █░░ █ █▄░█ █▀▀
    █▄▄ █▀█ █▄▀ █▀█ ▄█ ░█░ █▀▄ █▄█ ▄█   █▄▀ ██▄   █▀▄ ██▄ ▄█ ░█░ █▀█ █▄█ █▀▄ █▀█ █░▀█ ░█░ ██▄ ▄█   █▄█ █░▀█ █▄▄ █ █░▀█ ██▄""")
    print("")

def menu():
    print('\n1. Cadastrar Restaurante')
    print('2. Listar Restaurante')
    print('3. Ativar Restaurante')
    print('4. Sair')
   
def finalizar_app():
    print("\nFinalizando ...")
 
def opcao_invalida():
    print("\nDesculpe!Não temos essa opção em nosso sistema.\n")
    input("Digite enter para voltar ao menu principal")  
    main()
   
def cadastrar_restaurante():
    print("\n\nCadastre-se: ")
    nome_restaurante = input("Qual o nome do seu restaurante?: ")
    categoria_restaurante = input("Qual a categoria do restaurante?: ")
   
    dados_restaurante = {"nome" : nome_restaurante, "categoria" : categoria_restaurante, "ativo" : False}
    restaurantes.append(dados_restaurante)
    print(f"\nO {nome_restaurante} foi cadastrado com sucesso!")
    input("Digite enter para voltar ao menu principal")  
    main()
   
def listar_restaurantes():
    #print(f"\nAqui está a lista de restaurantes q estão cadastrados em nosso sistema: ")
    for restaurante in restaurantes:
        nome_restaurante = restaurante["nome"]
        categoria_restaurante = restaurante["categoria"]
        ativo_ou_nao = restaurante["ativo"]
        print(f"-->", nome_restaurante)
        print(f"-", categoria_restaurante)
        print(f"-", ativo_ou_nao, "\n")
           
    input("Digite enter para voltar ao menu principal")  
    main()

def alternar_estado_restaurante():
    print('Alternando o estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alternar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante["ativo"]
            mensagem = f'o restaurante {nome_restaurante} foi ativado com sucesso'if restaurante['ativo'] else f'o restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
        if not restaurante_encontrado:
            print('o restaurante nao foi encontrado')

def escolher_opção():
    try:
        opcao = int(input("\nEscolha uma opção: "))
               
        if(opcao == 1):
           cadastrar_restaurante()

        elif(opcao == 2):
            listar_restaurantes()
               
        elif(opcao == 3):
            alternar_estado_restaurante
               
        elif(opcao == 4):
            finalizar_app()
           
        else:
            opcao_invalida()
           
    except:
        opcao_invalida()

   
def main():
    os.system('cls')
    exibir_nome_do_programa()
    menu()
    escolher_opção()
   
if __name__ == '__main__':
    main()