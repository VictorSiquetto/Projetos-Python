# Exercício 107 – Exercitando módulos em Python

from modulos import moeda

p = float(input('Digite o preço: R$'))
print(f'O dobro de {p} é {moeda.dobro(p):.2f}')
print(f'A metade de {p} é {moeda.metade(p):.2f}')
print(f'Aumentando 13% de {p} é {moeda.aumentar(p, 13):.2f}')
print(f'Diminuindo 15% de {p} é {moeda.diminuir(p, 15):.2f}')
