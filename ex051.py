#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final mostre os 10 primeiros
#termos dessa progressão.

print('==' * 20)
print(f"{'10 TERMOS DE UMA PA' :^40}")
print('==' * 20)
n = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
termo = n + (10 - 1) * r
for c in range(n , termo + r , r):
    print(c, end = ' -> ')
print('ACABOU')