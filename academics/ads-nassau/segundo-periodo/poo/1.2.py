class Fila:
  def __init__(self):
    self.pessoas = []
  def entrar_fila(self, nome):
    self.pessoas.append(nome)
  def sair_fila(self):
   self.pessoas.pop(0)
  def visualizar_fila(self):
    return self.pessoas
mercado = Fila()
loteria = Fila()
mercado.entrar_fila('Ana')
loteria.entrar_fila('Antonio')
loteria.entrar_fila('Julia')
print(f'Fila do Supermercado: {mercado.visualizar_fila()}')
print(f'FIla da Loteria: {loteria.visualizar_fila()}')
