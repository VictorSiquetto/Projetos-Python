# Exercício 94 – Unindo dicionários e listas

dic = {}
lista = []
mulheres = []
tot = 0
while True:
    dic['nome'] = str(input('Nome: '))
    dic['sexo'] = ' '
    while dic['sexo'] not in 'MF':
        dic['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
        if dic['sexo'] not in 'MF':
            print('Erro, digite apenas M ou F')
        if dic['sexo'] == 'F':
            mulheres.append(dic['nome'])
    dic['idade'] = int(input('Idade: '))
    tot += dic['idade']
    lista.append(dic.copy())
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
        if opcao not in 'SN':
            print('Erro, digite apenas S ou N')
    if opcao == 'N':
        break
media = tot / (len(lista))
print('=-'*20)
print(f'Ao todo temos {len(lista)} pessoas cadastradas')
print(f'A media de idade é de {media:.2f} anos')
print('As mulheres cadastradas foram', end =' ')
for m in mulheres:
    print(m, end =' ')
print('\nLista das pessoas que estao acima da media: ')
for c in lista:
    if c['idade'] > media:
        print(f"Nome = {c['nome']}; Sexo = {c['sexo']}; Idade = {c['idade']}")
print('Encerrado')
