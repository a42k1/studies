catalogo = [] #lista de livros

def id_gen(): #gerador de id dos livros no catalogo
    return len(catalogo) + 1

def add_livro(): #função add livro
    titulo = input('Título: ')
    autor = input('Autor: ')
    data_pub = input('Ano de publicação: ')
    livro = {
      'id': id_gen(),
      'titulo': titulo,
      'autor': autor,
      'data_pub': data_pub,
      'disponivel': True
    }
    catalogo.append(livro)
    print('Livro cadastrado')

def show_livros(): #função para mostrar os livros no catalogo
    for livro in catalogo:
        status = "Disponivel" if livro['disponivel'] else "Emprestado"
        print(f'{livro['id']}: {livro['titulo']} - {livro['autor']} - {livro['data_pub']} - {status}')

def buscar_titulo(titulo): #função que busca o livro por titulo
    encontrados = [livro for livro in catalogo if titulo.lower() in livro['titulo'].lower()]
    if encontrados:
        for livro in encontrados:
            status = "Disponível" if livro['disponivel'] else "Emprestado"
            print(f"[{livro['id']}] {livro['titulo']} - {livro['autor']} ({livro['data_pub']}) - {status}")
    else:
        print("Nenhum livro encontrado com esse título.")

def atualizar_disp_livro(id_livro, disponivel): #função que atualiza a disponibilidade de livro
    for livro in catalogo:
        if livro['id'] == id_livro:
            livro['disponivel'] = disponivel
            return True
    return False

