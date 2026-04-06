# Desenvolva um programa que pergunte a distância que um passageiro deseja percorrer em km.
# Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até de 200 km, e R$
# 0,45 para viagens mais longas.
#--------------------------------------------------------------------

#Entrada
distancia = float(input('Digite a distanci que deseja percorrer: '))

if distancia <=200:
    valor = 0.50 * distancia
elif distancia > 200:
    valor = 0.45 * distancia

print(f'O valor da sua viagem ficou em R$ {valor}')