#Lista que guardará todos os contatos adicionados
agenda = []

def adicionar_contatos(novo_contato: dict) -> None:
  '''
  Descrição: Função para adicionar novo contato na agenda (lista). \n
  Parâmetro: A função recebe um novo_contato do tipo dict. \n
  Retorno: A função nao tem retorno.
  '''
  agenda.append(novo_contato)

def exibir_contatos() -> list:
  '''
    Descrição: Função retorna todos os contatos da agenda. \n 
    Parâmetro: A função não recebe valores no parâmetro. \n
    Retorno: A função retorna uma lista com todos os contatos.
  '''
  return agenda

def atualizar_telefone(contato: str, novo_numero: str) -> bool:
    for item in agenda:
        if item['nome'] == contato:
            item['telefone'] = novo_numero
            return True
    return False

