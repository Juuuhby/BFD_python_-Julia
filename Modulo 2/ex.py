# 2 - Suponha que estamos desenvolvendo um sistema para um banco. Este sistema deve obedecer as seguintes restrições:
# A - Uma classe pai chamada Cliente, com os atributos: nome, cpf, endereço.
# B - Uma classe filha chamada Conta_Corrente que deve herdar os atributos da classe pai mais o atributo "saldo". Este atributo deve ser privado.
# C - O sistema precisa ser capaz de: depositar, sacar, consultar saldo, consultar informações dos clientes e alterar informações dos clientes. Não deve ser possível ter saldo negativo, nem sacar além do saldo.
# Crie ao menos 1 instância de Conta_Corrente, execute todos os métodos para teste.

class Cliente:

    def __init__(self,nome,cpf,endereço):
        self.nome = nome
        self.cpf = cpf
        self.endereço = endereço

class Conta_corrente(Cliente):

    def __init__(self, nome, cpf, endereço,saldo):
        super().__init__(nome, cpf, endereço)
        self._saldo = saldo

    def depositar(self,deposito):
        self._saldo = self._saldo + deposito
        print(f"O seu saldo atual é {self._saldo}.")

    def sacar(self,saque):
        if self._saldo >= saque:
            self._saldo = self._saldo - saque
            print(f"Você sacou {saque}. O seu saldo atual é {self._saldo}.")
        else:
            print(f"Saldo insuficiente. O seu saldo é {self._saldo}.")

    def consultar_saldo(self):
        print(f"O seu saldo é {self._saldo}")

    def informaçao_cliente(self):
        print("====Informações do Cliente====")
        print(f"Nome do Cliente: {self.nome}")
        print(f"CPF: {self.cpf}")
        print(f"Endereço: {self.endereço}")
        print("==============================")

    def alterar_cliente(self,alteraçao):
        print("Para alterar informações, aperte: \n" \
        "A - Nome do Cliente \n" \
        "B - Endereço do Cliente \n")
        op = str(input("Insira a opção escolhida: "))
        if op == "A" or op == "a":
            self.nome = alteraçao
            print("O nome do cliente foi alterado.")
        if op ==  "B" or op == "b":
            self.endereço = alteraçao
            print("O endereço do cliente foi alterado.")
        else:
            print("Escolha uma opção válida.")
        
            
cliente1 = Conta_corrente("Julia Diniz","000.000.000-00","Rua Presidente Pedreira",1400)

cliente1.consultar_saldo()
cliente1.sacar(400)
cliente1.depositar(1700)
cliente1.informaçao_cliente()
cliente1.alterar_cliente("Rua Zumbi dos Palmares")
cliente1.informaçao_cliente()

