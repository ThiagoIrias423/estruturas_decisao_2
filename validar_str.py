# Desenvolva um programa que receba uma string e exiba a mesma na tela. Se o valor digitado for em branco exibir 'Dado inválido'
#----------------------------------------------------------------------------


entrada = input('Digite uma string: ')

if entrada.strip() == '':
    print('Dado inválido')
else:
    print(entrada)