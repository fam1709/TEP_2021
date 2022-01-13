# Felipe Menescal
# Online Judge
# 10104 Euclid Problem - Extended Euclidean algorithm : https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm
import sys

def extd_euclid(a,b):
    s = 0
    r = b
    old_s = 1
    old_r = a
    while(r != 0):
        quociente = old_r // r
        old_r , r = r , old_r - (quociente*r)
        old_s , s = s, old_s - (quociente*s)
    if(b != 0):
        y = (old_r - (old_s*a))/b
    else:
        y = 0
    x = old_s
    d = old_r
    return x , y , d

def main():
    entrada = sys.stdin.read().splitlines()
    for linha in entrada:
        linha = linha.split()
        a , b = int(linha[0]) , int(linha[1])
        x , y , d = extd_euclid(a,b)
        print(int(x),int(y),int(d))

if __name__=='__main__':
    main()