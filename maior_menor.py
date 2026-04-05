num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))

maior = max(num1, num2, num3)
menor = min(num1, num2, num3)
soma = num1 + num2 + num3
media = soma / 3

print(f'MAIOR = {maior}')
print(f'Menor = {menor}')
print(f'Soma = {soma}')
print(f'Media = {media}')