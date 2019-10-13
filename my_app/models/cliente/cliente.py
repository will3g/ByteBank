from my_app.models.endereco.endereco import Endereco

class Cliente(Endereco):

  __slots__ = ['__titular', '__cpf', '__email', '__telefone', '__celular', '__numero_residencial']

  __id = 0
  
  def __init__(self, nome, sobrenome, cpf, email, telefone, celular, endereco, complemento, numero_residencial, pais, estado, cep):
    Cliente.__id += 1
    self.__titular = nome + ' ' + sobrenome
    self.__cpf = cpf
    self.__email = email
    self.__telefone = telefone
    self.__celular = celular
    self.__numero_residencial = numero_residencial
    super().__init__(endereco, complemento, pais, estado, cep)

  @property
  def get_id(self):
    return self.__id

  @property
  def get_titular(self):
    return self.__titular

  @property
  def get_cpf(self):
    return self.__cpf

  @property
  def get_email(self):
    return self.__email

  @property
  def get_telefone(self):
    return self.__telefone

  @property
  def get_celular(self):
    return self.__celular

  @property
  def get_numero_residencial(self):
    return self.__numero_residencial