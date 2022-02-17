# Felipe Menescal
# Online Judge
# 10203 Snow Clearing - Euclid Circuit
import sys
from math import sqrt

def dist_calc(x1,y1,x2,y2):
    return sqrt((x2-x1)**2 + (y2-y1)**2)


def main():
    entrada = sys.stdin.read().splitlines()
    casos = int(entrada.pop(0))
    entrada.pop(0)
    sum_dist = 0
    j = 0
    for i in range(casos):
        while(entrada[j] != ''):
            linha = entrada[j]
            linha = linha.split()
            if(len(linha) == 2):
                j += 1
                continue
            else:
                sum_dist += dist_calc(int(linha[0]),int(linha[1]),int(linha[2]),int(linha[3]))
                j += 1
                if(j == len(entrada)):
                    break
        sum_dist *= 2
        sum_dist *= 3 # (sum_dist / 20) * 60 = sum_dist * 3
        km_percorridos = sum_dist/1000
        if(km_percorridos - int(km_percorridos) >= 0.5):
          km_percorridos += 1
        horas = int(km_percorridos)//60
        minutos = int(km_percorridos)%60
        if(minutos < 10):
          print(str(horas) + ':0' + str(minutos))
        else:
          print(str(horas) + ':' + str(minutos))
        sum_dist = 0
        j += 1
        if(j < len(entrada)):
            print('')
    

if __name__=='__main__':
    main()