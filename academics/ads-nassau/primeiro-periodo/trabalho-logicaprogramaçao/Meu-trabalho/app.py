from livro import *
from user import *
from emprestimo import *
#Aqui no app.py faço o menu com a interface que puxa todas as funções dos 3 arquivos principais (emprestimo.py, livro.py, user.py)

#Decidi organizar em sub-menus pra melhorar a clareza do sistema e ficar organizado entao temos três sub-menus e um principal.
def menu_livros():
    while True:
        print("\n--- MENU LIVROS ---")
        print("1 - Adicionar Livro")
        print("2 - Listar Livros")
        print("3 - Buscar Livro por Título")
        print("0 - Voltar ao Menu Principal")
        
        opt = input("Escolha: ")
        
        if opt == "1":
            add_livro() 
        elif opt == "2":
            show_livros()
        elif opt == "3":
            titulo = input("Digite o título a buscar: ")
            buscar_titulo(titulo)
        elif opt == "0":
            break
        else:
            print("Opção inválida.")
#Acima temos o sub-menu de livros onde fiz a interface e fiz callbacks das funções que estao em livro.py
def menu_usuarios():
    while True:
        print("\n--- MENU USUÁRIOS ---")
        print("1 - Adicionar Usuário")
        print("2 - Listar Usuários")
        print("3 - Buscar por ID")
        print("4 - Alterar Email de Usuário")
        print("0 - Voltar ao Menu Principal")
        
        opt = input("Escolha: ")
        
        if opt == "1":
            add_user()

        elif opt == "2":
            listar_user()

        elif opt == "3":
            id_user = int(input("ID do Usuário: "))
            buscar_user_id(id_user)

        elif opt == "4":
            id_user = int(input("ID do usuário: "))
            alt_email(id_user)

        elif opt == "0":
            break

        else:
            print("Opção inválida.")
#Acima temos o sub-menu de usuário.
def menu_emprestimos():
    while True:
        print("\n--- MENU EMPRÉSTIMOS ---")
        print("1 - Realizar Empréstimo")
        print("2 - Devolver Livro")
        print("3 - Listar Empréstimos Ativos")
        print("4 - Ver Histórico de Empréstimos")
        print("0 - Voltar ao Menu Principal")
        
        opt = input("Escolha: ")
        
        if opt == "1":
            emp_livro()
        elif opt == "2":
            dev_livro()
        elif opt == "3":
            list_emprestimos()
        elif opt == "4":
            id_user = int(input("ID do usuário: "))
            historico(id_user)
        elif opt == "0":
            break
        else:
            print("Opção inválida.")
#Acima o sub-menu de empréstimos.
def menu():
    while True:
        print("\n--- MENU PRINCIPAL ---")
        print("1 - Livros")
        print("2 - Usuários")
        print("3 - Empréstimos")
        print("4 - Sair")

        opt = input("Escolha: ")

        if opt == "1":
            menu_livros()
        elif opt == "2":
            menu_usuarios()
        elif opt == "3":
            menu_emprestimos()
        elif opt == "4":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida.")
#E por fim o menu principal onde o usuário escolhe pra onde vai.
menu() #Executa tudo.