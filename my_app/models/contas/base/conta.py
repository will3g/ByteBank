from my_app.models.errors.errors import ValorMenorQueZeroError, \
    TranferenciaNaoEfetuadaError, SaldoELimiteInsuficienteError
from my_app.models.contas.dateCreateAccount import DateCreateAccount
from my_app.models.contas.historico import Historico

class Conta:

    __slots__ = ['__numero',
                 '__titular',
                 '_saldo',
                 '__limite',
                 '__date_abertura',
                 '__historico',
                 '_identificador_conta',
                 '__senha']

    __quantidade_contas = 0
    
    def __init__(self, numero, senha, limite):
        self.__numero = numero
        self.__senha = senha
        self._saldo = 0.0
        self.__limite = limite
        self.__date_abertura = DateCreateAccount()
        print('Conta criada em {}'.format(self.__date_abertura.dateCreated()))
        self._identificador_conta = Conta.__quantidade_contas
        Conta.__quantidade_contas += 1
        self.__historico = Historico()

    def __str__(self):
        print('Titular: {} | Numero: {} | Saldo: {} | Limite: {} | Data abertura: {}'
            .format(self.__titular, self.__numero, self._saldo, self.__limite, self.__date_abertura))

    @property
    def _get_id(self):
        print('ID_Conta: {}'.format(self._identificador_conta))
        return self._identificador_conta

    @property
    def _quantidade_contas(self):
        print('Quantidade de contas: {}'.format(Conta.__quantidade_contas))
        return Conta.__quantidade_contas

    @property
    def get_saldo(self):
        return self._saldo

    @property
    def get_historico(self):
        self.__historico.imprime()

    @property
    def extrato(self):
        print('Titular: {}  Numero conta:  {}  Saldo:  {}  Limite: {}'
            .format(self.__titular, self.__numero, self._saldo, self.__limite))

    def __valida_valores_de_entrada(self, valor):
        if valor <= 0:
            raise ValorMenorQueZeroError('O parâmetro de entrada não pode ser menor que zero. Valor de entrada = {}'.format(valor))
        return True

    def depositar(self, valor):
        self.__valida_valores_de_entrada(valor)
        self._saldo += valor
        self.__historico.transacoes.append('Deposito de {} | Saldo de {}'.format(valor, self._saldo))
        return True

    def sacar(self, valor):
        self.__valida_valores_de_entrada(valor)
        _saldo_e_limite__ = self._saldo + self.__limite
        if valor > _saldo_e_limite__:
            raise SaldoELimiteInsuficienteError('Saldo e limite insuficientes para saque.')
        elif valor <= self._saldo:
            self._saldo -= valor
            self.__historico.transacoes.append('Saque de {} | Saldo de {}'.format(valor, self._saldo))            
            return True
        # else:
        #     self._saldo -= valor
        #     self._limite -= valor
        #     print('Sacou limite')
        #     return True

    def tranfere_para(self, conta_destino, valor):
        return_sacar = self.sacar(valor)
        if return_sacar:
            conta_destino.depositar(valor)
            self.__historico.transacoes.append('Valor transferencia de {} para conta {} | Saldo de {}'
                .format(valor, conta_destino.__numero, self._saldo))
            return True
        raise TranferenciaNaoEfetuadaError(
            'Tranferencia nao efetuada, falhou no método sacar. Retorno {}'
                .format(return_sacar))
        
    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa











'''######################################################################'''
if __name__ == '__main__':
    from conta import Conta

    cc = Conta(1234, 'ppp', 80, 500)
    cc1 = Conta(1234, 'ppp', 0, 500)

    try:
        cc.extrato()
        cc.tranfere_para(cc1, 50)
        cc.extrato()
    except ValorMenorQueZeroError as err:
        print(err)
    except SaldoELimiteInsuficienteError as err:
        print(err)
    
    