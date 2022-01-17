# Felipe Menescal
# Online Judge
# 11466 Largest Prime Divisor
import sys
from math import sqrt

# https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n
def primes1(n):
    """ Returns  a list of primes < n """
    sieve = [True] * (n//2)
    for i in range(3,int(sqrt(n))+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i] = [False] * ((n-i*i-1)//(2*i)+1)
    return [2] + [2*i+1 for i in range(1,n//2) if sieve[i]]

def main():
    entrada = sys.stdin.read().splitlines()
    primos = primes1(10000001)
    for linha in entrada:
        linha = int(linha)
        maior = -1
        divs = 0
        if(linha == 0):
            break
        if(linha < 0):
            linha = linha * -1
        aux = linha
        for p in primos:
            if(p > int(sqrt(aux))):
                break
            if(linha % p == 0):
                divs += 1
                maior = p
                while(linha % p == 0):
                    linha //= p
        if(linha != 1):
            maior = linha
            divs += 1
        if(divs <= 1):
            print('-1')
        else:
            print(str(maior))
            
if __name__=='__main__':
    main()