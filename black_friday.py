# Na última Black Friday, o gerente de uma loja de perfumes colocou todo o seu estoque em promoção, de acordo com a tabela a seguir:

# Código	Condição de Pagamento	Desconto (%)
# 1 	À vista (em espécie) 	10
# 2	Cartão de débito	5
# 3	Cartão de crédito	3
# 4	PIX			7.5
#---------------------------------------------------------------------

#Entrada

valor_total = float(input('Digite o valor total da ventda: '))

print('******************')
print('FORMA DE PAGAMENTO')
print('******************')
print('1. À vista (em espécie) \n2. Cartão de débito \n3. Cartão de crédito \n4. Pix')
print('*********************')

forma_pagamento = int(input('Digite a opção desejada: '))

if forma_pagamento == 1:
    desconto = 0.1
elif forma_pagamento == 2:
    desconto = 0.05
elif forma_pagamento == 3:
    desconto = 0.03
elif forma_pagamento == 4:
    desconto = 0.075
else:
    ('Opção inválida')

print(f'O valor final a ser pago é R$ {valor_total - (desconto*100):.2f}')