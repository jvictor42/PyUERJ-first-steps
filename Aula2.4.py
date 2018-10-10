# Exercício 4 Aula 2
#Um laser vermelho (com comprimento de onda lambda = 632.8 nm) incide em uma fenda dupla produzindo um padrão de interferência com franjas claras e escuras, em um anteparo situado a uma distância D = 1.98m da fenda. Calcule a distância DeltaY entre dois máximos consecutivos de interferência. Considere o espaçamento entre as fendas, d=0.250mm. <em>Dica: a distância entre dois máximos de interferência consecutivos pode ser aproximada por Delta y = \frac{\lambda D}{d}$.


#unidade de comprimento em nm(10^-9)
lmbd=632.8
Dist=1.98*(10**9)
d=25*(10**4)
delta_y=(lmbd*Dist)/d


print('Qual distância entre 2 maximos consecutivos, produzido por interferencia de onda?')
print('lambida=632.8nm, distância do anteparo=1.98m, distância entre fendas = 0.25mm:')
print(delta_y,'nm ou,',delta_y/(10**6),'mm')
print('Fim!')
