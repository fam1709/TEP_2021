# Felipe Menescal
# Online Judge
# 615 Is It A Tree?

import sys
from collections import deque

def busca_largura(adjs, raiz):
    fila = deque()
    explor = 1
    fila.append(raiz)
    while(fila):
        v = fila.popleft()
        for w in adjs[v]:
            fila.append(w)
            explor += 1
    return explor


def main():
    entrada = sys.stdin.read().splitlines()
    adjs = {}
    case = 1
    for linha in entrada:
        if(linha == ''):
            case += 1
            adjs = {}
            continue
        linha = deque(linha.split())
        while(linha):
            par1, par2 = int(linha.popleft()), int(linha.popleft())
            if(par1 < 0 or par2 < 0):
                break
            if(par1 == 0 and par2 == 0):
                if(not adjs):
                    print('Case ' + str(case) + ' is a tree.')
                    continue
                else:
                    oco = 0
                    raiz = 0
                    isTree = True
                    for k in adjs.keys():
                        for g in adjs.values():
                            if(k in g):
                                oco += g.count(k)
                        if(oco > 1):
                            isTree = False
                            break
                        if(oco == 0):
                            raiz = k
                        oco = 0
                    if(not isTree):
                        print('Case ' + str(case) + ' is not a tree.')
                        continue
                    if(not raiz):
                        print('Case ' + str(case) + ' is not a tree.')
                        continue
                    explor = busca_largura(adjs, raiz)
                    if(explor == len(adjs)):
                        print('Case ' + str(case) + ' is a tree.')
                    else:
                        print('Case ' + str(case) + ' is not a tree.')

            else:
                if(par1 not in adjs):
                    adjs[par1] = []
                if(par2 not in adjs):
                    adjs[par2] = []
                adjs[par1].append(par2)

if __name__=='__main__':
    main()