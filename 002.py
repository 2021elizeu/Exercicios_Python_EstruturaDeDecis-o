"""Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo."""

n1 = int(input('Digite um numero:'))

if (n1 > 0):
    print (f'Numero positivo: {n1}.')
elif(n1 < 0):
    print (f'Numero negativo:{n1}.')
else:
    print('O numero é nulo')