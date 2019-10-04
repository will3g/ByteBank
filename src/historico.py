class Historico():

  def __init__(self):
    self.transacoes = []

  def imprime(self):
     print('Transacoes: ')
     for transacao in self.transacoes:
       print('-', transacao)