def cadastrar_usuario(usuarios):
    nome = input("Informe o nome do cliente: ")
    data_nascimento = input("Informe a data de nascimento (dd/mm/aaaa): ")
    cpf = input("Informe o CPF: ")
    endereco = input("Informe o endereço (logradouro, número, bairro, cidade/sigla): ")

   
    if any(user['cpf'] == cpf for user in usuarios):
        print("CPF já cadastrado. Não é possível cadastrar o mesmo CPF novamente.")
        return None

    usuario = {"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco}
    usuarios.append(usuario)
    print("Usuário cadastrado com sucesso!")


def cadastrar_conta(contas, agencia, usuarios):
    cpf = input("Informe o CPF do titular da conta: ")
    usuario_encontrado = next((user for user in usuarios if user['cpf'] == cpf), None)

    if usuario_encontrado:
        numero_conta = len(contas) + 1  # Calcula o número da conta sequencialmente
        conta = {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario_encontrado}
        contas.append(conta)
        print("Nova conta cadastrada com sucesso!")
    else:
        print("CPF não encontrado. Por favor, cadastre o usuário primeiro.")


def saque(saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("Saque realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato


def listar_contas(contas):
    for conta in contas:
        print(f"Agência: {conta['agencia']}, Conta: {conta['numero_conta']}, CPF do titular: {conta['usuario']['cpf']}")


menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[nu] Novo Usuário
[nc] Nova Conta
[l] Listar Contas
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
numero_conta = 0  

usuarios = []  
contas = []  

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("Depósito realizado com sucesso!")
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        saldo, extrato = saque(saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUES)

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "nu":
        cadastrar_usuario(usuarios)

    elif opcao == "nc":
        cadastrar_conta(contas, "0001", usuarios)

    elif opcao == "l":
        listar_contas(contas)

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
