#!python
# Atualizar lista de programas
import os

os.system('pip list --outdated > list_program_upgrad.txt')

arquivo = open('list_program_upgrad.txt', 'r', encoding='utf8')

lista = []
for dado in arquivo:
    if dado.split()[0] == '------------------------':
        continue
    elif dado.split()[0] == 'Package':
        continue
    else:
        lista.append(dado.split()[0])
arquivo.close()
print(lista)

for conteudo in lista:
    os.system(f'pip install --upgrade {conteudo}')
