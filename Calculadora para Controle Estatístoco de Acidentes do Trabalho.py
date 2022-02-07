horas= int(input('Digite o número de horas trabalhadas:'))
empregados= int(input('Digite o número de empregados:'))
H= horas * empregados

DP= int(input('Digite o número de Dias Perdidos (DP):'))
DD= int(input('Digite o número de Dias Debitados (DD):'))
D = DP + DD

N = int(input('Digite o número de acidentados com lesões e afastamentos (N):'))
IAG = DP / N

Tf = N * 1000000 / H
Tg = D * 1000000 / H

print('------------------------------------------------------------------------------------')
print(f'H (Horas-homens de exposição ao risco) {H: .2f}:')
print(f'D (Tempo Computado): {D: .2f}:')
print(f'Tf (Taxa de Frequencia de Acidentados com Lesão) {Tf: .2f}:')
print(f'Tg (Taxa de Gravidade)= {Tg: .2f}')
print(f'IAG (Índice de Avaliação de Gravidade): {IAG: .2f}')