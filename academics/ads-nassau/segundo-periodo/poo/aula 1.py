class Fila:
  def __init__(self):
    self.pessoas = []
  def entrar_fila(self, nome):
    self.pessoas.append(nome)
  def sair_fila(self):
   self.pessoas.pop(0)
  def visualizar_fila(self):
    return self.pessoas
# Criando um objeto tipo FIla chamado supermercado
supermercado = Fila()
supermercado.entrar_fila('Ana')
supermercado.entrar_fila('Pedro')
supermercado.sair_fila()
print(supermercado.visualizar_fila())
