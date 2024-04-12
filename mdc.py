print('Ola, este arquivo verifica o mdc entre dois números naturais.')
a = int(input('Digite seu primeiro número natural:'))
b = int(input('Digite seu segundo número natural: '))
# A variavel "dc" vai representar os divisores candidatos...
# eh feito a busca em ordem dcrescente dos divisores em comum,
# de modo que o primeiro divisor ser  será o nosso maximo divisor comum
dc = a
# O valor "dc" pode ser inicializado tanto com os valores de entrada de "a", quanto os valores de entrada de "b"
# Para testar se o numero de entrada é um divisor comum entre a e b, vamos pegar o resto da divisão de a e para testar se é divisor de b vamos usar o operador logico end para ligar
while not (a%dc == 0 and b%dc==0):
    dc = dc-1
# Criei um laço para decrementar
print('O MDC entre:(%d, %d)=%d'%(a,b,dc))
