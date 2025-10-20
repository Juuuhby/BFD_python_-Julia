# 1 - Construa uma classe para armazenar informações de carros, cada objeto instanciado por essa classe deve ter os seguintes atributos:
# A - Modelo, marca, ano de lançamento, potência (1.0,1.6,etc), tipo de câmbio (manual ou automático), preço no lançamento.
# B - Crie um método para retornar cada atributo.
# Crie ao menos 3 instâncias de objeto, e execute todos os métodos para teste.

class Carros:

    def __init__(self,modelo,marca,ano_lançamento,potencia,tipo_cambio,preço_lançamento):
        self.modelo = modelo
        self.marca = marca
        self.ano_lançamento = ano_lançamento
        self.potencia = potencia
        self.tipo_cambio = tipo_cambio
        self.preço_lançamento = preço_lançamento

    def ficha_tecnica(self):     
        print("------------------Ficha Técnica------------------------")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Ano de Lançamento: {self.ano_lançamento}")
        print(f"Potência: {self.potencia}")
        print(f"Tipo de câmbio: {self.tipo_cambio}")
        print(f"Preço no ano de Lançamento: {self.preço_lançamento}")
        print("-------------------------------------------------------")
        
    def modelo_carro(self):
        print(self.modelo)

    def marca_carro(self):
        print(self.marca)
        
    def ano_carro(self):
        print(self.ano_lançamento)

    def pot(self):
        print(self.potencia)

    def cambio(self):
        print(self.tipo_cambio)

    def preço(self):
        print(self.preço_lançamento)

        
car1 = Carros("Lancer","Mitsubishi",2016,2.0,"Automatico","R$68.990")
car2 = Carros("A3","Audi",2016,1.4,"Automatico","R$137.990")
car3 = Carros("Impala","Chevrolet",1967,155,"Automatico","US$3.300")

car1.ficha_tecnica()
car2.ficha_tecnica()
car3.ficha_tecnica()
car3.ano_carro()
car3.cambio()
car3.marca_carro()
car3.modelo_carro()
car3.preço()
car3.pot()


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

