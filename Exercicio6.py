#EXERCICIO 6:  Índice de Massa Corporal (IMC):O usuário deve digitar seu peso (em kg) e altura (em metros) para calcularmos o IMC dele usando a fórmula: IMC = peso / (altura^2). Tendo em vista
# estes valores classifique o resultado em categorias (abaixo do peso, peso normal, sobrepeso, obesidade) com base na tabela de índices IMC.

peso = float(input("Digite seu peso (em kg): "))
altura = float(input("Digite sua altura (em metros): "))

imc = peso / (altura ** 2)

if imc < 18.5:
    print("Você está abaixo do peso.")
elif imc < 24.9:
    print("Você está com peso normal.")
elif imc < 29.9:
    print("Você está com sobrepeso.")
elif imc < 34.9:
    print("Você está com obesidade grau I.")
elif imc < 39.9:
    print("Você está com obesidade grau II.")
else:
    print("Você está com obesidade grau III.")