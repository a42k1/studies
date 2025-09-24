users = [] #lista de usuarios

def id_gen(): #gerador de id para a lista de usuarios
    return len(users) + 1

def add_user(): #função para add usuários
  nome = input('Nome: ')
  email = input('E-Mail: ')
  for u in users:
      if u['email'] == email:
          print('Esse e-mail ja existe.')
          return
  user = {
      'id': id_gen(),
      'nome': nome,
      'email': email
  }
  users.append(user)
  print('Usuários cadastrado.')

def listar_user(): #função para listar os usuários
    for u in users:
      print(f"{u['id']}: {u['nome']} - {u['email']}")  

def buscar_user_id(id_user): #buscar usuários por id de usuário
    for u in users:
        if u['id'] == id_user:
            print(f"{u['id']}: {u['nome']} - {u['email']}")
            return u
    print("Usuário não encontrado.")
    return None

def alt_email(id_user): #função para alterar email do usuário
    novo_email = input("Novo e-mail: ")
    for u in users:
        if u['id'] == id_user:
            u['email'] = novo_email
            print('Email atualizado')
            return
    print('Usuário não encontrado.')