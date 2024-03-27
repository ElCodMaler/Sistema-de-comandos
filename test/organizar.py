variable = input('valores: ')
lista = list
print(type(variable))

if '"' in variable:
    lista = variable.split('"')
else:
    print('1/2 carton :/')
print()
for l in lista:
    print(l)