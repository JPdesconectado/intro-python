#!/usr/bin/python3

# LISTS
# https://docs.python.org/3/tutorial/introduction.html#lists

# list slicing [inicio:fim:passo]

weekdays = ['mon','tues','wed','thurs','fri']

print(weekdays)
print(type(weekdays))

days = weekdays[0]         # elemento 0
days = weekdays[0:3]       # elementos 0, 1, 2
days = weekdays[:3]        # elementos 0, 1, 2
days = weekdays[-1]        # ultimo elemento

test = weekdays[3:]        # elementos 3, 4

weekdays

days = weekdays[-2]        # ultimo elemento (elemento 4
days = weekdays[::]        # all elementos
days = weekdays[::2]       # cada segundo elemento (0, 2, 4)
days = weekdays[::-1]      # reverso (4, 3, 2, 1, 0)

all_days = weekdays + ['sat','sun']     # concatenar

print(all_days)

# Usando append
days_list = ['mon','tues','wed','thurs','fri']
days_list.append('sat')
days_list.append('sun')

print(days_list)
print(days_list == all_days)

list = ['a', 1, 3.14159265359]
print(list)
print(type(list))
# list.reverse()
# print(list)

#########
# Exercicios - Listas
# Faca sem usar loops
#########

print("--------------------")
print("Exercícios")

# Como selecionar 'wed' pelo indice?
print("Questão 01:", days_list[2])

# Como verificar o tipo de 'mon'?
print("Questão 02:", type(days_list[days_list.index('mon')]))

# Como separar 'wed' até 'fri'?
a = days_list.index('wed')
b = days_list.index('fri')+1
print("Questão 03:", days_list[a:b])

# Quais as maneiras de selecionar 'fri' por indice?
print("Questão 04:", days_list[4])

# Qual eh o tamanho dos dias e days_list?
print("Questão 05:", len(days_list))

# Como inverter a ordem dos dias?
days_list.reverse()
print("Questão 06:", days_list)

# Como inserir a palavra 'zero' entre 'a' e 1 de list?
list.insert(1, 'zero')
print("Questão 07:", list)

# Como atribuir o ultimo elemento de list na variavel ultimo_elemento e remove-lo de list?
ultimo_elemento = list.pop()
print("Questão 08:", list)
print('Ultimo elemento que fora removido: ', ultimo_elemento)

# Como limpar list?
list.clear()
print("Questão 09:", list)

# Como deletar list?
del(list)
print("Questão 10: Lista Deletada.")