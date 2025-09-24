class Fila:
  fila_geral = []
  def __init__(self):
    self.pessoas = []
  def entrar_fila(self, nome):
    self.pessoas.append(nome)
  def sair_fila(self):
   self.pessoas.pop(0)
  def visualizar_fila(self):
    return self.pessoas
  @classmethod
  def entrar_fila_geral(cls, nome):
    cls.fila_geral.append(nome)

Fila.entrar_fila_geral('Raimundo')
print(Fila.fila_geral)

