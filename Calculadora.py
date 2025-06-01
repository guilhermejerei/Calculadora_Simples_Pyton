import math

def soma(a, b):
    return a + b

def subtrai(a, b):
    return a - b

def multiplica(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Erro: Divisão por zero!"
    return a / b

def potencia(a, b):
    return a ** b

def raiz_quadrada(a):
    return a ** 0.5

def fatorial(a):
    return math.factorial(int(a))

switch = {
    1: "Soma",
    2: "Subtração",
    3: "Multiplicação",
    4: "Divisão",
    5: "Potência",
    6: "Raiz Quadrada",
    7: "Fatorial"
}

def calcular(opcao, resultado_anterior=None):
    operacoes_binarias = {
        1: soma,
        2: subtrai,
        3: multiplica,
        4: divide,
        5: potencia
    }

    if opcao in operacoes_binarias:
        if resultado_anterior is not None:
            num1 = resultado_anterior
            print(f"\nUsando resultado anterior: {num1}")
        else:
            num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        func = operacoes_binarias[opcao]
        return func(num1, num2)

    elif opcao == 6 or opcao == 7:
        if resultado_anterior is not None:
            num = resultado_anterior
            print(f"\nUsando resultado anterior: {num}")
            return raiz_quadrada(num) if opcao == 6 else fatorial(num)
        else:
            if opcao == 6:
                num = float(input("Digite o número para calcular a raiz quadrada: "))
                return raiz_quadrada(num)
            else:
                num = int(input("Digite o número para calcular o fatorial: "))
                return fatorial(num)

nome = input("Digite seu nome: ")
print(f"\nOlá, {nome}! Bem-vindo à Calculadora!")

resultado_atual = None


print("\nDigite qual operação você deseja realizar:")
for key in switch:
    print(f"{key} - {switch[key]}")

while True:
    try:
        opcao = int(input("\nDigite o número da operação: "))
        if opcao in switch:
            break
        else:
            print("Opção inválida! Tente novamente.")
    except ValueError:
        print("Entrada inválida! Digite um número inteiro.")

print(f"\nVocê escolheu: {switch[opcao]}")
resultado_atual = calcular(opcao, resultado_atual)
print(f"\nResultado: {resultado_atual}")

while True:  # Loop principal do programa
    
    if resultado_atual is None:
        print("\nDigite qual operação você deseja realizar:")
        for key in switch:
            print(f"{key} - {switch[key]}")
        
        while True:
            try:
                opcao = int(input("\nDigite o número da operação: "))
                if opcao in switch:
                    break
                else:
                    print("Opção inválida! Tente novamente.")
            except ValueError:
                print("Entrada inválida! Digite um número inteiro.")
        
        resultado_atual = calcular(opcao, resultado_atual)
        print(f"\nResultado: {resultado_atual}")

    print("\nO que você deseja fazer agora?")
    print("1 - Continuar usando o resultado atual")
    print("2 - Zerar e começar nova operação")
    print("3 - Sair da calculadora")

    escolha = input("\nDigite sua escolha (1/2/3): ")
    if escolha == "1":
        print("\nVocê escolheu continuar usando o resultado atual.")
        for key in switch:
            print(f"{key} - {switch[key]}")
        opcao = int(input("\nDigite o número da nova operação: "))
        if opcao in switch:
            resultado_atual = calcular(opcao, resultado_atual)
            print(f"\nResultado: {resultado_atual}")
        else:
            print("Opção inválida! Tente novamente.")
    elif escolha == "2":
        resultado_atual = None
        print("\nVocê escolheu realizar uma nova operação.")
    elif escolha == "3":
        print("\nObrigado por usar a calculadora! Até a próxima.")
        break
    else:
        print("Escolha inválida! Tente novamente.")
        continue
