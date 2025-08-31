'''Pegue a data de vencimento do boleto
 e diga quantos dias faltam para o vencimento'''
# AUTOR: VITOR KAUÊ
# DATA: 20/03/2023
import datetime # Importa o módulo datetime

print("="*40)
print("      CALCULADORA DE BOLETO")
print("="*40)

#INPUTS
data_vencimento = input("Digite a data de vencimento do boleto (dd/mm/aaaa): ")

#CALCULOS
dia, mes, ano = map(int, data_vencimento.split('/'))
data_vencimento = datetime.datetime(ano, mes, dia)
data_hoje = datetime.datetime.now()
dias_faltando = (data_vencimento - data_hoje).days

# PRINTS
print("\n" + "-"*40)
print(f"A data de vencimento do boleto é {data_vencimento.strftime('%d/%m/%Y')}.")
print(f"Faltam {dias_faltando} dias para o vencimento.")
print("-"*40)