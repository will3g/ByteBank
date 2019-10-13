from my_app.models.contas.base.conta import Conta
from my_app.models.cliente.cliente import Cliente
import random

class ContaCorrente(Conta):

  __id = 0

  def __init__(self, titular):
    ContaCorrente.__id += 1
    self.__numero = random.randrange(0, 9999999999999999)
    self.titular = titular
    self.limite = 1500.0
    self.__senha = random.randrange(0, 99999)
    Conta.__init__(self, titular=self.titular, numero=self.__numero, senha=self.__senha, limite=self.limite)

  def atualiza(self, taxa):
    self._saldo += self._saldo * taxa * 3

  @property
  def get_numero(self):
    return self.__numero

  @property
  def get_tipo_conta(self):
    return 'Conta corrente'

  @property
  def get_senha(self):
    return self.__senha

  @property
  def get_limite(self):
    return self.limite

  @property
  def get_cliente(self):
    return Cliente