class Endereco():

    __id = 0

    __slots__ = ['__endereco', '__complemento', '__pais', '__estado', '__cep']

    def __init__(self, endereco, complemento, pais, estado, cep):
        Endereco.__id += 1
        self.__endereco = endereco
        self.__complemento = complemento
        self.__pais = pais
        self.__estado = estado
        self.__cep = cep

    @property
    def get_id(self):
        return self.__id

    @property
    def get_endereco(self):
        return self.__endereco

    @property
    def get_complemento(self):
        return self.__complemento

    @property
    def get_pais(self):
        return self.__pais

    @property
    def get_estado(self):
        return self.__estado

    @property
    def get_cep(self):
        return self.__cep
