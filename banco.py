class ContaBancaria:
    def __init__(self):
        self.saldo = 500.0
        self.saques_restantes = 3

    def depositar(self, valor):
        if valor <= 0:
            print("Valor de depósito inválido.")
        else:
            self.saldo += valor
            print(f"Depósito de R$ {valor:.2f} realizado. Novo saldo: R$ {self.saldo:.2f}")

    def sacar(self, valor):
        if self.saques_restantes > 0:
            if valor <= 0:
                print("Valor de saque inválido.")
            elif valor > self.saldo:
                print("Saldo insuficiente.")
            else:
                self.saldo -= valor
                self.saques_restantes -= 1
                print(f"Saque de R$ {valor:.2f} realizado. Novo saldo: R$ {self.saldo:.2f}")
        else:
            print("Limite de saques atingido.")

    def extrato(self):
        print(f"Saldo: R$ {self.saldo:.2f}")
        print(f"Saques restantes: {self.saques_restantes}")

# Função para mostrar as opções ao usuário
def mostrar_opcoes():
    print("Opções:")
    print("1. Depositar")
    print("2. Sacar")
    print("3. Extrato")
    print("0. Sair")

# Exemplo de uso
conta = ContaBancaria()

while True:
    mostrar_opcoes()
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        valor_deposito = float(input("Digite o valor do depósito: "))
        conta.depositar(valor_deposito)
    elif opcao == 2:
        valor_saque = float(input("Digite o valor do saque: "))
        conta.sacar(valor_saque)
    elif opcao == 3:
        conta.extrato()
    elif opcao == 0:
        print("Encerrando o programa.")
        break
    else:
        print("Opção inválida. Digite novamente.")
