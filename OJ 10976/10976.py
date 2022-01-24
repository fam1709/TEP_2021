# Felipe Menescal
# Online Judge
# 10976 Fractions Again ?!

import sys
from math import sqrt

def primo(num):
    if(num <= 1):
        return False

    for i in range(2, int(sqrt(num)) + 1):
        if(not num % i):
            return False
    return True

def main():
    entrada = sys.stdin.read().splitlines()
    for linha in entrada:
        linha = int(linha)
        ans = ''
        y = linha + 1
        x = linha * y
        ans += '1/' + str(linha) + ' = ' + '1/' + str(x) + ' + ' + '1/' + str(y) + '\n'
        if(x == y):
            print('1')
            print(ans[:-1])
            continue
        while(y <= linha * 2):
            y += 1
            if(primo(y)):
                continue
            if((linha*y) % (y - linha) == 0):
                x = (linha*y) // (y - linha)
                ans += '1/' + str(linha) + ' = ' + '1/' + str(x) + ' + ' + '1/' + str(y) + '\n'
        ans = ans.splitlines()
        print(len(ans))
        for l in ans:
            print(l)

if __name__=='__main__':
    main()