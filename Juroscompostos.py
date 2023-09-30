valor_inicial = float(input())
taxa_juros = float(input())
periodo = int(input())

valor_final = valor_inicial

valor_final = (1+taxa_juros)
valor_final = valor_final**periodo
valor_final = valor_inicial*valor_final
#valor_final= valor_final+valor_inicial

print("Valor final do investimento: R$", "%.2f" % valor_final)