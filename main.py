MENU = {
    "espresso": {
        "ingredientes": {
            "agua": 50,
            "cafe": 18,
        },
        "preco": 2.5,
    },
    "latte": {
        "ingredientes": {
            "agua": 200,
            "leite": 150,
            "cafe": 24,
        },
        "preco": 5.5,
    },
    "cappuccino": {
        "ingredientes": {
            "agua": 250,
            "leite": 100,
            "cafe": 24,
        },
        "preco": 6.0,
    }
}

recursos_maquina = {
    "agua": 300,
    "leite": 200,
    "cafe": 100,
}

lucro = 0


def verifica_recursos(ordem_ingrediente):
    """Retorna  True quando o pedido pode ser feito, False se os ingredientes forem insufucientes."""
    for item in ordem_ingrediente:
        if ordem_ingrediente[item] > recursos_maquina[item]:
            print(f"Desculpe o {item} esta em falta!.")
            return False
    return True


def procesas_moedas():
    """Returns the total calculated from coins inserted."""
    print("Por favor insira as moedas: ")
    total = int(input("quantas de 10 centavos?: ")) * 0.1
    total += int(input("quantas de 25 centavos?: ")) * 0.25
    total += int(input("quantas de 50 centavos?: ")) * 0.5
    total += int(input("quantas de 1 real?: ")) * 1
    return total


def verifica_transacao(pagamento_recebido, custo_bebida):
    """Retorna True quando apgamento foi aceito, ou False se o pagamento foi insuficiente"""
    if pagamento_recebido >= custo_bebida:
        arredondameto = round(pagamento_recebido - custo_bebida, 2)
        print(f"Aqui esta ${arredondameto} de troco.")
        global lucro
        lucro += custo_bebida
        return True
    else:
        print("Desculpe dinehiro insufuciente, o dinheiro foi retornado!")
        return False


def fazer_cafe(nome_bebida, ordem_ingrediente):
    """Deduz os ingredientes necessários dos recursos da maquina."""
    for item in ordem_ingrediente:
        recursos_maquina[item] -= ordem_ingrediente[item]
    print(f"Aqui esta seu {nome_bebida} ☕️. Bom aproveito!")


ligada = True

while ligada:
    escolha = input("Escolha sua bebida? (espresso/latte/cappuccino): ")
    if escolha == "desligar":
        ligada = False
    elif escolha == "relatorio":
        print(f"Agua: {recursos_maquina['agua']}ml")
        print(f"Leite: {recursos_maquina['leite']}ml")
        print(f"Cafe: {recursos_maquina['cafe']}g")
        print(f"Dinheiro: ${lucro}")
    else:
        bebida = MENU[escolha]
        if verifica_recursos(bebida["ingredientes"]):
            pagamento = procesas_moedas()
            if verifica_transacao(pagamento, bebida["preco"]):
                fazer_cafe(escolha, bebida["ingredientes"])
