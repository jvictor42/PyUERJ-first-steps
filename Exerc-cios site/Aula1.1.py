#Exercício 1 Aula 1
#Se você fizer uma corrida de 10 quilômetros em 43 minutos e 30 segundos, qual será seu tempo médio por milha? Qual é a sua velocidade média em milhas por hora? (Dica: há 1,61 quilômetros em uma milha).
d_m=10*1000
t_s=43*60+30
#velocidade em m/s
v_ms=d_m/t_s
l=1610
#velociodade em km/h
v_kmh=v_ms*3.6
#velocidade em libras/h
v_lh=v_kmh/l
#tempo por libra
t_l=(l*t_s)/d_m
#apresentação dos valores
print(d_m,'m e ',t_s,'s tem v=',v_ms,'m/s')
print('ou em libras:')
print(v_lh,'L/h, com um tempo de ', t_l,'seg. por libra')
print('Fim!')
