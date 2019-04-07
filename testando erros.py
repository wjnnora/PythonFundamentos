try:
    num1 = int(input("Digite um número: "))
    num2 = int(input("Digite um número: "))
    assert num1 != 0
except:
    print("Você digitou o número zero.")