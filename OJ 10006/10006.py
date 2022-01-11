# Felipe Menescal
# Online Judge
# 10006 Carmichael Numbers
import sys

#def crivo_eras(n):
#    m = (n-1) // 2
#    boole = [True]*m
#    i,pot,lista_primos = 0,3,[2]
#    while pot*pot < n:
#        if(boole[i]):
#            lista_primos.append(pot)
#            j = 2*i*i + 6*i + 3
#            while j < m:
#                boole[j] = False
#                j = j + 2*i + 3
#        i = i + 1
#        pot = pot + 2
#    while i < m:
#        if(boole[i]):
#            lista_primos.append(pot)
#        i = i + 1
#        pot = pot + 2
#    return lista_primos
#primos = crivo_eras(65000)

def main():
    entrada = sys.stdin.read().splitlines()
    carmichael = [561,1105,1729,2465,2821,6601,8911,10585,15841,29341,41041,46657,52633,62745,63973]
    for linha in entrada:
        if (linha == '0'):
            break
        if(int(linha) in carmichael):
            print('The number ' + linha + ' is a Carmichael number.')
        else:
            print(linha + ' is normal.')
        #if(int(linha) in primos):
        #    print(linha + ' is normal')
        #else:
        #    res = crivo_eras(int(linha))
        #    if(len(res) >= 3):
        #        print('The number ' + linha + ' is a Carmichael number.')
        #    else:
        #        print(linha + ' is normal')

if __name__ == '__main__':
	main()