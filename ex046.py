from time import sleep
from emoji import emojize
print('-=' * 24)
print('CONTAGEM REGRESSIVA PARA OS FOGOS DE ARTIFICIO:')
print('-=' * 24)
for c in range (10 , 0 - 1 , -1):
    sleep(1)
    print(c)
sleep(1.5)
print(emojize("BOOM :collision:", language='alias'))