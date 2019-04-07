from Pessoa import Pessoa

continuar = 1
lista_pessoas = []

while(continuar == 1):
    try:
        nome = str(input("Digite seu nome: "))
        sobrenome = str(input("Digite seu sobrenome: "))
        idade = int(input("Digite sua idade: "))

        pessoa = Pessoa(nome, sobrenome, idade)

        continuar = int(input("\nDeseja continuar?\n"
              "1 - Continuar\n"
              "0 - Sair"))
    except ValueError:
        print("Digite um número válido.")

else:
    for x in lista_pessoas:
        print(f"Nome completo: {x.nome} {x.sobrenome} - Idade: {x.idade}")