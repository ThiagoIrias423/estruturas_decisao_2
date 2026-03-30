# Desenvolva um programa que pergunte a velocidade do carro de um usuário. 
# Se a velocidade ultrapassar 80km/h, exiba uma mensagem dizendo que o usuário foi multado. 
# Nesse caso, exiba o valor da multa, cobrando R$ 50,00 por cada km acima de 80 km/h.
# Exemplo: Digite a velocidade em Km/h: 85
# Limite = 80Km/h
# Excedeu 5Km/h
# multa = 5Km/h * R$ 50,00
# Valor da multa: R$ 250,00
#--------------------------------------------------------------------------

#Entrada
velocidade = float(input('Digite a velocidade do seu carro: '))

#Processamento
if velocidade > 80:
    excedeu = velocidade - 80
    valor_da_multa = excedeu * 50.00
else:
    print('Você não foi multado')

#saida
print('---------------')
print('Limtite: 80km/h')
print('--------------------------')
print(f'excedeu {excedeu:.2f}km/h')
print('-----------------------------')
print(f'multa = {excedeu} * R$ 50,00')
print('-----------------------------')
print(f'Valor da multa: R$ {valor_da_multa:.2f}')