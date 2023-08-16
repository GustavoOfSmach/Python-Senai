#EXERCICIO 2: O usuário deve digitar um número, após este processo verifique se o número é positivo, negativo ou igual a zero, e exiba a mensagem correspondenteao número.

numero =int(input("Insira um Numero: "))

if numero > 0:
    print("O número é positivo.")
elif numero < 0:
    print("O número é negativo.")
else:
    print("O número é igual a zero.")

