saldo_atual = float(input('Digite seu saldo atual:'))
valor_depositado = float(input('Digite o valor de deposito:'))
valor_retirada = float(input('Digite o valor de retirada:'))

#Vamos calcular quanto a pessoa tem

total=saldo_atual+valor_depositado
total=total-valor_retirada

print("Saldo atualizado na conta:", total)

