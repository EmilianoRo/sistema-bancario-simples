menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_de_saques = 0
limite_de_saques = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        try:
            valor_deposito = float(input("Digite o valor do depósito: "))
        except ValueError:
            print("Valor inválido. Digite um número.")
            continue

        saldo += valor_deposito
        extrato += f"Depósito R$ {valor_deposito:.2f}\n"
        print(f"Depósito no valor de R$ {valor_deposito:.2f} realizado com sucesso!")

    elif opcao == "s":
        try:
            valor_sacar = float(input("Digite o valor do saque: "))
        except ValueError:
            print("Valor inválido. Digite um número.")
            continue

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

    elif opcao == "e":
        print(extrato)
        print(f"Saldo: R$ {saldo:.2f}")

    elif opcao == "q":
        break

    else:
        print("Operação inválida. Por favor, selecione uma opção válida.")
