from my_app.models.contas.base.conta import Conta
from my_app.models.cliente.cliente import Cliente

class ContaCorrente(Conta, Cliente):

  def __init__(self):
    self.titular = Cliente.get_titular
    self.saldo = 50.0
    self.limite = 1500.0
    if self.titular != '' and self.titular != None:
      Conta.__init__(self, titular=self.titular, saldo=self.saldo, limite=self.limite)
    else:
      print('Deu ruim!')

  def atualiza(self, taxa):
    self._saldo += self._saldo * taxa * 3