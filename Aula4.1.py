#Aula 4 exercicio 1 site
#Crie uma função que imprima na tela a data de hoje em português (Utilize a libraria time e a função localtime, que tipo de objeto ela retorna?
import time
a=time.localtime()
ano=a.tm_year
mes=a.tm_mon
dia=a.tm_mday
hora=a.tm_hour
min=a.tm_min
sem=a.tm_wday
def semana(x):
    f_sem=['segunda-feira', 'terça-feira', 'quarta-feira','quinta-feira', 'sexta-feira']
    return f_sem[x]
print('Hora:',hora,':',min,
       'Data:',dia,'/',mes,'/',ano, semana(sem))
print('Fim!')
