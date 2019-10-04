class AtualizadorDeContas:
  
  def __init__(self, selic, saldo_total=0):
    self.__selic = selic
    self.__saldo_total = saldo_total

  def roda(self, conta):
    print('Saldo anterior: R${} reais'.format(conta.get_saldo))
    conta.atualiza(self.__selic)
    print('Saldo atual: R${} reais'.format(conta.get_saldo))
