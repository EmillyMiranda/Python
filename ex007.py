print('Relação de nota e média.\n gerada por aluno')
n1 = float (input('L.portuguesa: '))
n2 = float (input('Matematica: '))
n3 = float (input('Ciências: '))
n4 = float (input('História: '))
n5 = float (input('Química: '))
m = float ((n1 + n2 + n3 + n4 + n5)/5)
print(f'A media geral do aluno é {m}')
if m > 6:
    print('Aprovado')
else:
    print('Reprovado')
    