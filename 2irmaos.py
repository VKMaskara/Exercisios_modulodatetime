'''Faça um programa que pergunte a idade de dois irmãos e 
diga qual a diferença de idade entre eles.'''
# AUTOR: VITOR KAUÊ
# DATA: 20/03/2023

import datetime # Importa o módulo datetime

print("="*40)
print("         CALCULADORA DE IDADE ENTRE IRMÃOS")
print("="*40)

#INPUTS
nome1 = input("Digite o nome do primeiro irmão: ")
idade1 = int(input(f"Digite a idade de {nome1}: "))
nome2 = input("Digite o nome do segundo irmão: ")
idade2 = int(input(f"Digite a idade de {nome2}: "))

#CALCULOS
diferenca_idade = abs(idade1 - idade2)

# PRINTS
print("\n" + "-"*40)
print(f"A diferença de idade entre {nome1} e {nome2} é de {diferenca_idade} anos.")
print("-"*40)