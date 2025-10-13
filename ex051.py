#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final mostre os 10 primeiros
#termos dessa progressão.

n = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
for c in range(1,10+1):
    termo = n + (c - 1) * r
    print(termo)