#EXERCICIO 7: Calcular descontos:Quando o usuário digitar o valor total de sua compra e um percentual de descontoaplicado. Você deve calcularo valor com desconto e mostraro resultadopara ele.

total = float(input("Digite o valor total da compra: "))
percentual_desconto = float(input("Digite um percentual de desconto aplicado: "))

desconto = total * percentual_desconto / 100

valor_com_desconto = total - desconto

print(f"O valor com desconto é {valor_com_desconto}.")