#Faça um programa que leia um número inteiro e mostre na tela 
#o seu sucessor e antecessor

digito = int(input('Digite um número: '))
sucessor = digito + 1
antecessor = digito - 1
#print('o número escolhido é {}, o seu sucesso é {} e o antecessor {}' .fomart(digito,sucessor,antecessor))
print('O número escolhido é {}, o número que vem depois é {} o que vem antes é {}' .format(digito, sucessor, antecessor))