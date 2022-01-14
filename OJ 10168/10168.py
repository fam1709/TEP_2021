# Felipe Menescal
# Online Judge
# 10168 Summation of Four Primes
import sys

# https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n
def primes1(n):
    """ Returns  a list of primes < n """
    sieve = [True] * (n//2)
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i] = [False] * ((n-i*i-1)//(2*i)+1)
    return [2] + [2*i+1 for i in range(1,n//2) if sieve[i]]


def main():
    entrada = sys.stdin.read().splitlines()
    primos = set(primes1(10000000))
    for linha in entrada:
        if(int(linha) < 8):
            print('Impossible.')
        else:
            # par (2 2)
            linha = int(linha) - 4
            if(linha%2 == 0):
                for num in primos:
                    if((linha - num) in primos):
                        print('2 2 ' + str(num) + ' ' + str(linha-num))
                        break
                
            # par (2 3)
            else:
                linha -= 1
                for num in primos:
                    if((linha - num) in primos):
                        print('2 3 ' + str(num) + ' ' + str(linha-num))
                        break

if __name__=='__main__':
    main()