#Exercício 2 Aula 1
#Desde sua varanda você escuta o som do primeiro fogo artificial do reveillon 3 segundos depois de ver a luz, qual a distância? (o som tem velocidade 343 m/s e a luz 3x10^8 m/s).
tsom=3
t0=0
v_som=343
c=3*10**8
#Distância dos fogos, assumindo tluz instante 0
d_som=v_som*(tsom-t0)
#Achando distância real
t_luz=d_som/c
d_real=v_som*(tsom-t_luz)
#Apresentação dos resultados
print('Desde sua varanda você escuta o som do primeiro fogo artificial do reveillon 3 segundos depois de ver a luz, qual a distância?')
print('distância assumindo t0=0, ',d_som,'m ou achando t0 real, ',d_real,'m')
print('Fim!')
