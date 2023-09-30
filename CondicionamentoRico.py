saldo_total = int(input())
valor_saque = int(input())

if (valor_saque<saldo_total):
    print('Saque realizado com sucesso.'  "Novo Saldo:", saldo_total-valor_saque)
else:
    print("Saldo insuficiente. Saque nao realizado!")
    