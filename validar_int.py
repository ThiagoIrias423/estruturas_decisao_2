# Desenvolva um programa que receba um inteiro e exiba o mesmo na tela. Se o valor digitado for em branco exibir 'Dado inválido'
#-------------------------------------------------------

num1 = input('Digite um número inteiro: ').strip()

if num1 == "":
    print('Dado inválido')
else:
    num = int(num1)
    print(num1)
    