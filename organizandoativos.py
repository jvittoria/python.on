ativos = []

# Entrada da quantidade de ativos
quantidadeAtivos = int(input())

# Entrada dos códigos dos ativos
for quantidadeAtivos in range(quantidadeAtivos):
    codigoAtivo = input()
    ativos.append(codigoAtivo)
# TODO: Ordenar os ativos em ordem alfabética.
sorted_ativos = sorted(ativos)
# TODO: Imprimir a lista de ativos ordenada, conforme a tabela de exemplos.
for ativo in sorted_ativos:
    print(ativo)