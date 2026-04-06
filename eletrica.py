# Uma empresa, que presta serviço à companhia de energia elétrica do estado, necessita de um programa que auxilie os seus eletricistas no cálculo das principais grandezas da Eletricidade
# que são Tensão, Resistência e Corrente. Sabe-se que:
# U = R * I, 
# onde, 
# U é a Tensão      (em V), 
# R é a Resistência (em Ώ) e,
# I é a Corrente    (em A).

# Você foi contratado(a) pela empresa para atender a essa solicitação.
# Construa um programa que apresente o seguinte menu:
#-----------------------------------------------------------------------

#Entrada
print('******************************')
print('CÁLCULO DE GRANDEZAS ELÉTRICAS')
print('******************************')
print('1. Tensão')
print('2. Resistência')
print('3. Corrente')
print('4. Sair do programa')
print('******************************')

opcao = int(input('Digite uma opção: '))

if  opcao == 1:
    resitencia = float(input('Digite a resistência do circuito: '))
    corrente = float(input('Digite a corrente od circuito: '))
    tensao = resitencia * corrente
elif opcao == 2:
    tensao = float(input('Digite a tensão: '))
    corrente = float(input('Digite a corrente od circuito: '))
    resitencia = tensao / corrente
elif opcao == 3:
    tensao = float(input('Digite a tensão: '))
    resitencia = float(input('Digite a resistência do circuito: '))
    corrente = tensao / resitencia
elif opcao == 4:
    print('Você saiu do programa')
else:
    print('Erro')

print(f'tensão: {tensao:.2f} Volts')
print(f'Resistência: {resitencia:.2f} Ohms')
print(f'Corrente: {corrente:.2f} Ampéres')