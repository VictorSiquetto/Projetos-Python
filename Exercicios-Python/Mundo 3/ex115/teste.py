from modulos.funcoes import *
from time import sleep

while True:
    resp = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    if resp == 1:
        titulo('Opcao 1')
    elif resp == 2:
        titulo('Opcao 2')
    elif resp == 3:
        titulo('Saindo do Programa')
        break
    else:
        print(f'\033[31mERRO: por favor digite uma opcao valida\033[0m')
    sleep(2)
