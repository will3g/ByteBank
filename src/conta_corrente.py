from conta import Conta

class ContaCorrente(Conta):

  def __init__(self, numero, titular, saldo, limite):
    super().__init__(numero, titular, saldo, limite)
  
  def atualiza(self, taxa):
    self._saldo += self._saldo * taxa * 2