def soma(n1, n2): 
    return n1 + n2

def subtracao(n1, n2):
    return n1 - n2

def multiplicacao(n1, n2):
    return n1 * n2

def divisao(n1, n2):
    return n1/n2

def menu():
    print(' 1-Soma  \n 2- Subtrai \n 3- Multiplica \n 4- Divide \n 5- Sair')
    operacao = int(input())
    while(operacao<1 or operacao>5):
        print("Opção Invalida")
        operacao = int(input())
    return operacao

def escolha(operacao, n1, n2):
    if operacao == 1: 
        result = soma(n1, n2)
    elif operacao == 2:
        result = subtracao(n1, n2)
    elif operacao == 3: 
        result = multiplicacao(n1, n2)
    elif operacao == 4: 
        if n2 != 0:
            result = divisao(n1, n2)
        else:
            result = None
    return result

def entrada():
    return int(input())

def main():
    while True: 
        operacao = menu()
        if operacao == 5:
            break
        print('Digite 2 números')
        n1 = entrada()
        n2 = entrada()
        if escolha(operacao, n1, n2) == None:
            print('Não há divisão por zero')
        else:
            print(escolha(operacao, n1, n2))

main()