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