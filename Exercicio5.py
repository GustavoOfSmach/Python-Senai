#EXERCICIO 5: Converter temperatura:Peça ao usuário para digitar uma temperatura em graus Celsius, depois deste
#passo converta essa temperatura para Fahrenheit usando a fórmula: Fahrenheit = (Celsius * 9/5) + 32e apresentar a temperatura convertida na tela.

celsius = float(input("Digite a temperatura em graus Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"A temperatura em Fahrenheit é {fahrenheit} graus.")
