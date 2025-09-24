class ContaBancaria:
  #Limitador de atributos da classe
  __slots__ = ['agencia', 'numero', 'titular', '__saldo']
  # Metodo inicializador
  def __init__(self, agencia, numero, titular):
    self.agencia = agencia
    self.numero = numero
    self.titular = titular
    self.__saldo = 0.0
  def depositar(self, valor):
    if valor > 0:
      self.__saldo += valor #(self) saldo = saldo + valor
      return True
    return False
  def sacar(self, valor):
    if self.__saldo >= valor:
      self.__saldo -= valor
      return True 
    return False
  def cons_saldo(self):
    return self.__saldo
  

conta1 = ContaBancaria('0023-x', '33355-2', 'Ana')
print(conta1.cons_saldo())
conta1.depositar(220)
conta1.sacar(110)
print(conta1.cons_saldo())

  
