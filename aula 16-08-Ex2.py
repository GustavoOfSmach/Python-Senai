#EXERCICIO 2: O usuário deve digitar um número e você deverá verificar se o número é par ou ímpar exibindo a mensagem adequada no terminal.

number = int(input("Coloque um número: "))

if number % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")

