# Felipe Menescal
# Online Judge
# 10608 Friends

import sys
from collections import deque

def busca_largura(adjs, vert, visitas):
    fila = deque()
    explor = 1
    fila.append(vert)
    visitas[vert] = True
    while(fila):
        v = fila.popleft()
        if(v not in visitas):
            visitas[v] = True
        for w in adjs[v]:
            if(w not in visitas):
                fila.append(w)
                explor += 1
                visitas[w] = True
    return explor


def main():
    entrada = sys.stdin.read().splitlines()
    adjs = {}
    casos = int(entrada.pop(0))
    pares = -1
    for linha in entrada:
        if(linha == ''):
            continue
        if(casos == 0):
            break
        if(pares == -1):
            linha = linha.split()
            cids, pares = int(linha[0]), int(linha[1])
            visitas = {}
            amigos = []
            adjs = {}
            if(pares == 0):
                print(1)
                pares = -1
                casos -= 1
                continue
            if(cids == 1):
                print(1)
                pares = -1
                casos -= 1
                continue
        else:
            linha = linha.split()
            par1, par2 = int(linha[0]) , int(linha[1])
            pares -= 1
            if(par1 not in adjs):
                adjs[par1] = []
            if(par2 not in adjs):
                adjs[par2] = []
            if(par2 not in adjs[par1]):
                adjs[par1].append(par2)
            if(par1 not in adjs[par2]):
                adjs[par2].append(par1)
            if(pares == 0):
                for k in adjs.keys():
                    if(k not in visitas):
                        amigos.append(busca_largura(adjs, k, visitas))
                print(max(amigos))
                pares = -1
                casos -= 1
        

if __name__=='__main__':
    main()