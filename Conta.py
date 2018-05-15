class Conta:

    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Saldo de {} do titular {}".format(self.saldo, self.titular))

    def deposita(self, valor):
        self.saldo += valor
        print("Novo saldo é de {} reais".format(self.saldo))

    def saca(self, valor):
        self.saldo -= valor
        print("Novo saldo é de {} reais".format(self.saldo))

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)