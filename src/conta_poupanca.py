from conta import Conta

class ContaPoupanca(Conta):

  def __init__(self, numero, titular, saldo, limite):
    super().__init__(numero, titular, saldo, limite)
  
  def atualiza(self, taxa):
    self._saldo += self._saldo * taxa * 3