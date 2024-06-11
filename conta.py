menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
[nu] Usuario
[nc] Conta
=> """

saldo = 0
limite = 500
extrato = ""
numero_de_saques = 0
limite_de_saques = 3
usuarios = []
agencia = "0001"
contas = []

def deposito(valor_deposito, saldo, extrato, /):
    saldo += valor_deposito
    extrato += f"Depósito R$ {valor_deposito:.2f}\n"
    print(f"Depósito no valor de R$ {valor_deposito:.2f} realizado com sucesso!")

def sacar(*, saldo, valor_sacar, extrato, limite, numero_de_saques, limite_de_saques):
    if saldo >= valor_sacar and valor_sacar <= limite and numero_de_saques < limite_de_saques:
        saldo -= valor_sacar
        numero_de_saques += 1
        extrato += f"Saque R$ {valor_sacar:.2f}\n"
        print(f"Saque no valor de R$ {valor_sacar:.2f} realizado com sucesso!")
    elif saldo < valor_sacar:
        print("Saldo insuficiente. Tente outra opção.")
    elif valor_sacar > limite:
        print(f"Seu limite de saque é de R$ {limite:.2f}")
    else:
        print("Limite de saques diário excedido.")

def exibir_extrato(saldo, /, *, extrato):
    print(extrato)
    print(f"Saldo: R$ {saldo:.2f}")

def criar_usuario(usuarios):

    cpf = input("imforme seu numero do cpf")
    usuarios = filtrar_usuario(cpf, usuarios)

    if(usuarios):
        print("já existe um usuario com este cpf")
        return
    nome = input("informe o nome completo")
    data_nascimento = input("informe a data de nascimento (dd-mm-aaaa)")
    endereco = input("informe o seu endereço (logradoro, nro - bairro - cidade - estado)")
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "endereco": endereco})

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_da_conta, usuarios):
    cpf = input("informe o cpf do usuario")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("conta criada com sucesso")
        return {"agencia": agencia, "numero_da_conta": numero_da_conta, "usuario": usuario}
    print("usuario nao encontrado criação de conta encerrado")

while True:
    opcao = input(menu)

    if opcao == "d":
        valor_deposito = float(input("Digite o valor do depósito: "))
        saldo, extrato = deposito(valor_deposito, saldo, extrato)

    elif opcao == "s":
        valor_sacar = float(input("Digite o valor do saque: "))
        saldo, extrato = sacar(
            saldo=saldo,
            valor_sacar=valor_sacar,
            extrato=extrato,
            numero_saques=numero_de_saques,
            limite_de_saque=limite_de_saques

        )
    
    elif opcao == "nu":
        criar_usuario(usuarios)
    
    elif opcao == "nc":
        numero_da_conta = len(contas) +1
        conta = criar_conta(agencia, numero_da_conta, usuarios)

        if conta:
            contas.append(conta)
            
    elif opcao == "e":
        exibir_extrato(saldo, extrato=extrato)

    elif opcao == "q":
        break

    else:
        print("Operação inválida. Por favor, selecione uma opção válida.")
