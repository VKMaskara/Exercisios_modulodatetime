''' pegue a data de nascimento do usuário,
mostre quantos anos tem e quanto tera em 2050'''
# AUTOR: VITOR KAUÊ
# DATA: 20/03/2023

import datetime # Importa o módulo datetime

print("="*40)
print("      CALCULADORA DE IDADE")
print("="*40)

#INPUTS
name = input("Digite seu nome: ") # Pede o nome do usuário
nasci = input("Digite sua data de nascimento (dd/mm/aaaa): ") # Pede a data de nascimento

#CALCULOS 
dia, mes, ano = map(int, nasci.split('/')) # Divide a string em dia, mês e ano
data_nascimento = datetime.datetime(ano, mes, dia)
data_hoje = datetime.datetime.now() # Pega a data atual
idade = data_hoje.year - data_nascimento.year # Calcula a idade
idade_em_2050 = 2050 - data_nascimento.year # Calcula a idade em 2050

# PRINTS
print("\n" + "-"*40)
print(f"Prazer, {name}!") # Saudação ao usuário
print(f"Você tem {idade} anos.") # Mostra a idade atual
print(f"Em 2050 você terá {idade_em_2050} anos.") # Mostra a idade em 2050
print("-"*40)