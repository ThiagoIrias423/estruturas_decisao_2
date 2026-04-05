litros = float(input('Digite Quantos litros irá abastecer: '))
preco_gasolina = 4.95
preco_alcool = 2.89
print('G - Gasolina\nA - Álcool')

opcao = input('Digite o tipo de Combustivél: ')

if litros <= 20 and opcao == 'G':
    preco = preco_gasolina
    desconto = 0.03 
elif litros > 20 and opcao == 'G':
    preco_gasolina
    desconto = 0.05
elif litros <= 20 and opcao == 'A':
    preco = preco_alcool
    desconto = 0.04
elif litros > 20 and opcao == 'A':
    preco = preco_alcool
    Ddesconto = 0.06

valor_bruto = litros * preco
valor_desconto = valor_bruto * desconto
valor_final = valor_bruto - valor_desconto

print(f'O valor bruto ficou em: R$ {valor_bruto:.2f}')
print(f'O valor do desconto ficou em R$ {valor_desconto:.2f}')
print(f'E o total a ser pago ficou em R$ {valor_final:.2f}')



