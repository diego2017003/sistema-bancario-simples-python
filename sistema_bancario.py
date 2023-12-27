from datetime import datetime


class SistemaBancario:
    def __init__(self, usuarios):
        self.usuarios = usuarios

    def create_new_usuario(self, usuario):
        self.usuarios.append(usuario)


class Usuario:
    def __init__(self, nome, saldo_inicial):
        self.nome = nome
        self.saldo = saldo_inicial
        self.dia_atual = datetime.today()
        self.saques_restantes = 3
        self.extrato = []

    def depositar(self, valor_deposito):
        if valor_deposito > 0:
            self.saldo = self.saldo + valor_deposito
            operacao = {"operacao": "deposito", "valor": valor_deposito}
            self.extrato.append(operacao)
        else:
            print("valor de deposito invalido")

    def sacar(self, valor_a_sacar):
        if self.saques_restantes > 0:
            if valor_a_sacar <= 500 and valor_a_sacar > 0:
                if valor_a_sacar <= self.saldo:
                    self.saldo = self.saldo - valor_a_sacar
                    operacao = {"operacao": "saque", "valor": valor_a_sacar}
                    self.extrato.append(operacao)
                    self.saques_restantes = self.saques_restantes - 1
                else:
                    print("valor de saque invalido")
            else:
                print("valor de saque invalido")
        else:
            print("não permite mais saques hoje")

    def extrato(self):
        return self.extrato

    def mudou_o_dia(self):
        if self.dia_atual != datetime.today():
            self.saques_restantes = 3
            self.dia_atual = datetime.today()

    def imprimir_extrato(self):
        print("Extrato")
        for valores in self.extrato:
            print(f"{valores['operacao']}-{valores['valor']}")
