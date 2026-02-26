# Exercício 113 – Funções aprofundadas em Python

def leiaInt(msg):
    ok = False
    while not ok:
        try:
            n = str(input(msg)).strip()
            ok = True
            return int(n)
        except:
            print(f'\033[31mERRO: por favor digite um numero valido\033[0m')
            ok = False
        
def leiaFloat(msg):
    ok = False
    while not ok:
        try:
            n = str(input(msg)).strip().replace(',', '.')
            ok = True
            return float(n)
        except:
            print(f'\033[31mERRO: por favor digite um numero valido\033[0m')
            ok = False

n1 = leiaInt('Digite um numero inteiro: ')
n2 = leiaFloat('Digite um numero real: ')
print(f'O valor inteiro digitado foi {n1:.1f} e o real foi {n2:.1f}')
