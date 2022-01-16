# Felipe Menescal
# Online Judge
# 10139 Factovisors
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
    primos = primes1(47000)
    for linha in entrada:
        linha = linha.split()
        n , m = int(linha[0]) , int(linha[1])
        if(m == 0 or m == 1):
            print(str(m) +  ' divides ' + str(n) +'!')
            continue
        if(n == 0):
            print(str(m) +  ' does not divide ' + str(n) +'!')
            continue
        prime_factors_n = {}
        prime_factors_m = {}       
        for p in primos:
            if(p > m):
                break
            count = 0
            while(m%p == 0):
                count += 1
                m /= p
            if(count != 0):
                prime_factors_m[p] = count
            if(m == 1):
                break
        if(not prime_factors_m):
            prime_factors_m[m] = 1
        if(int(m) != 1):
            prime_factors_m[m] = 1
        for k in prime_factors_m.keys():
            count = 0
            pow = k
            while(pow <= n):
                count += (n//pow)
                pow *= k
            prime_factors_n[k] = count
        aux = True
        for k,v in prime_factors_m.items():
            if(k not in prime_factors_n):
                aux = False
                break
            if(v > prime_factors_n[k]):
                aux = False
                break
        if(aux):
            print(str(int(linha[1])) +  ' divides ' + str(n) +'!')
        else:
            print(str(int(linha[1])) +  ' does not divide ' + str(n) +'!')

if __name__ == '__main__':
	main()
