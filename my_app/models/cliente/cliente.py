'''from models.contas.base.conta import Conta
from models.contas.tipos.conta_corrente import ContaCorrente
from models.contas.tipos.conta_poupanca import ContaPoupanca

from models.contas.atualizador_de_contas import AtualizadorDeContas'''

class Cliente():

  __id = 0
  
  def __init__(self, nome, sobrenome, cpf):
    Cliente.__id += 1
    self.__titular = nome + ' ' + sobrenome
    self.__cpf = cpf
    '''self.conta = ContaPoupanca(1234, self.__titular, 1000, 500)'''

  @property
  def get_id(self):
    return self.__id

  @property
  def get_titular(self):
    return self.__titular

  @property
  def get_cpf(self):
    return self.__cpf

'''if __name__ == "__main__":
  cliente = Cliente('José', 'da Silva', '2225-6')
  cliente2 = Cliente('Maria', 'do Rosário', '2225-6')

  adc = AtualizadorDeContas(0.01)

  adc.roda(cliente.conta)
  adc.roda(cliente.conta)
  
  print(cliente.conta.get_saldo)
  print(cliente.conta.get_saldo)

  cliente.conta.extrato
  cliente2.conta.extrato
  
  cliente.conta.tranfere_para(cliente2.conta, 40)
  
  cliente.conta.extrato
  cliente2.conta.extrato

  cliente.conta.get_historico
  cliente2.conta.get_historico

  cliente.conta._get_id
  cliente2.conta._get_id'''
