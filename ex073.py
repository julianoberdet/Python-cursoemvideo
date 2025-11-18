times = ('Palmeiras','Flamengo','Cruzeiro','Mirassol','Bahia','Botafogo','Fluminense','São Paulo',
'Vasco','Corinthians','Atlético-MG','Bragantino','Grêmio','Ceara','Internacional','Vitória','Santos',
'Juventude','Fortaleza','Sport')
print('-=' * 60)
print(f'Times do Brasileirão Serie A 2025: \033[35m{times}\033[m')
print('-=' * 60)
print(f'Os primeiros 5 times são: \033[32m{times[0:5]}\033[m')
print('-=' * 60)
print(f'Os 4 ultimos times são:\033[31m{times[-4:]}\033[m')
print('-=' * 60)
print(f'A lista em ordem alfabética :\033[33m{sorted(times)}\033[m')
print('-=' * 60)
print(f'O internacional está na \033[34m{times.index('Internacional')+1}ª\033[m posição')
