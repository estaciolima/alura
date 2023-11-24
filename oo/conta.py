class Conta:
    def __init__(self, numero, titular, saldo, limite=1000):
        print("Construindo o objeto...")
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        self.__codigo_banco = "001"
    
    def extrato(self):
        print("Saldo de R$ {} do titular {}".format(self.__saldo, self.__titular))

    def deposita(self, valor):
        self.__saldo += valor
        self.extrato()
    
    def __pode_sacar(self, valor):
        valor_disponivel = self.__saldo + self.__limite
        return valor <= valor_disponivel

    def saca(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
            self.extrato()    
        else:
            print("Saldo insuficiente")

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    @property
    def saldo(self):
        return self.__saldo
    
    @property
    def limite(self):
        print("This is the property method!")
        return self.__limite
    
    @limite.setter
    def limite(self, limite):
        print("This is the setter method!")
        self.__limite = limite

    @property
    def titular(self):
        return self.__titular.capitalize()
    
    @staticmethod
    def codigo_banco():
        return "001"
    
    @staticmethod
    def codigos_bancos():
        return {'BB':'001', 'Caixa':'104', 'Bradesco':'237'}
    
    