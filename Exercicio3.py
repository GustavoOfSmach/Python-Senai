#EXERCICIO 3: O usuário deve digitar dois números e uma operação matemática (+, -, *, /). Realize a operação solicitada e mostre o resultadona tela.

number1 = int(input("Coloque o primeiro número: "))
number2 = int(input("Coloque o segundo número: "))
operation = input("Insira a operação matemática (+, -, *, /): ")

if operation == "+":
    result = number1 + number2
elif operation == "-":
    result = number1 - number2
elif operation == "*":
    result = number1 * number2
elif operation == "/":
    result = number1 / number2

print(f"O resultado da operação foi que {number1} {operation} {number2} é {result}.")
