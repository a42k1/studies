class Estoque:
  __slots__ = ['data', 'quantidade', 'item', 'solicitante']
  def __init__(self, data, quantidade, item, solicitante):
    self.data = data
    self.quantidade = quantidade
    self.item = item
    self.solicitante = solicitante
