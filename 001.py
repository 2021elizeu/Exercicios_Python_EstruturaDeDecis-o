"""Faça um Programa que peça dois números e imprima o maior deles."""


n1 = int(input('Digite o primeiro numero:'))
n2 = int(input('Digite o segundo numero:'))


if (n1 > n2): #Função condicional SE
    print (f'o primeiro numero digitado {n1} é maior que o segundo {n2}.')
elif (n2 > n1): #Função condicional 
    print (f'o segundo numero digitado {n2} é maior que o primeiro {n1}.')
else: #Função condicional SE NÃO
    print('Os números são iguais.')