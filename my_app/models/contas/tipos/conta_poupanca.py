from my_app.models.contas.base.conta import Conta
from my_app.models.cliente.cliente import Cliente

class ContaPoupanca(Conta, Cliente):

  def __init__(self, numero, limite):
    Conta.__init__(self, numero, limite)
  
  def atualiza(self, taxa):
    self._saldo += self._saldo * taxa * 3