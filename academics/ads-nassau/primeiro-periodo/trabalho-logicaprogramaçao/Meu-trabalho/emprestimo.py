from livro import *
from user import *

emprestimos = [] #Lista dos emprestimos

def gerar_id(): #Função de geração de id
    return len(emprestimos) + 1

def emp_livro(): #função de emprestar livros
    id_livro = int(input("ID do livro: "))
    id_user = int(input("ID do usuário: "))
    for livro in catalogo:
        if livro['id'] == id_livro and livro['disponivel']:
            emprestimo = {
                'id': gerar_id(),
                'id_livro': id_livro,
                'id_user': id_user,
                'data_emprestimo': input("Data do empréstimo (DD-MM-AAAA): "),
                'data_devolucao': None
            }
            emprestimos.append(emprestimo)
            atualizar_disp_livro(id_livro, False)  # Usando a função
            print("Livro emprestado!")
            return
    print("Livro não disponível ou não encontrado.")

def dev_livro(): #Função de devolução
    id_emp = int(input("ID do empréstimo: "))
    for emp in emprestimos:
        if emp['id'] == id_emp and emp['data_devolucao'] is None:
            emp['data_devolucao'] = input("Data da devolução (DD-MM-AAAA): ")
            atualizar_disp_livro(emp['id_livro'], True)  # Usando a função
            print("Livro devolvido!")
            return
    print("Empréstimo não encontrado.")

def list_emprestimos(): #função de listar os empréstimos ativos.
    for emp in emprestimos:
        if emp['data_devolucao'] is None:
            livro = next((l for l in catalogo if l['id'] == emp['id_livro']), None)
            user = next((u for u in users if u['id'] == emp['id_user']), None)
            if livro and user:
                print(f"[{emp['id']}] {livro['titulo']} - {user['nome']} - {emp['data_emprestimo']}")

def historico(id_user): #funçâo para visualizar o historico de emprestimos.
    encontrados = [emp for emp in emprestimos if emp['id_user'] == id_user]
    if encontrados:
        for emp in encontrados:
            livro = next((l for l in catalogo if l['id'] == emp['id_livro']), None)
            status = "Devolvido" if emp['data_devolucao'] else "Ativo"
            print(f"{livro['titulo']} ({emp['data_emprestimo']}) - {status}")
    else:
        print("Nenhum empréstimo encontrado para esse usuário.")
