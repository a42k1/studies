from agenda import adicionar_contatos, exibir_contatos, atualizar_telefone

while True:
  opcao = int(input('Informe sua opção (1- Adicionar contato, /n 2- Exibir contato, 3- Atualizar contato: '))
  if opcao == 1:
    #Receber os dados
    nome = input('Informe um nome: ')
    telefone = input('Informe um número: ')
    email = input('Informe um e-mail: ')

    #Organizar em um dicionário
    contato = {
      'nome': nome,
      'telefone': telefone,
      'email': email
    }
    # Chamada da função para adicionar na agenda
    adicionar_contatos(contato)
  elif opcao == 2:
    agenda = exibir_contatos()
    print(agenda)
  
  elif opcao == 3:
    contato = input('Informe o contato a ser atualizado: ')
    novo_numero = input('Informe o novo número: ')
    #Chamada da função
    status = atualizar_telefone(contato, novo_numero)
    
    if status:
      print('Contato atualizado com sucesso.')
    else:
      print('Contato não encontrado.')
  
