# Felipe Menescal
# Online Judge
# 11085 Back to the 8-Queens
import sys
from copy import deepcopy

solucoes = []

def espaco_possivel(nova_lin, nova_col, posicoes):
    col_ant = 1
    while(col_ant <= (nova_col - 1)):
        lin_ant = posicoes[col_ant - 1]
        if(lin_ant == nova_lin):
            return False
        dist_lin = abs(lin_ant - nova_lin)
        dist_col = abs(col_ant - nova_col)
        if(dist_lin == dist_col):
            return False
        col_ant += 1
    return True

def solucao(col, posicoes):
    global solucoes
    for i in range(1,9):
        if(espaco_possivel(i,col+1, posicoes)):
            posicoes[col] = i
            if(col < 7):
                solucao(col+1, posicoes)
            else:
                aux = deepcopy(posicoes)
                solucoes.append(aux)
 

def main():
    entrada = sys.stdin.read().splitlines()
    casos = 1
    tabuleiro_ini = [1,1,1,1,1,1,1,1]
    solucao(0, tabuleiro_ini)
    global solucoes
    for linha in entrada:
        total = 0
        linha = list(map(lambda l : int(l), linha.split()))
        if(linha in solucoes):
            print('Case ' + str(casos) + ': ' + str(total))
            casos += 1
        else:
            for sol in solucoes:
                moves = 0
                for k in range(8):
                    if(sol[k] != linha[k]):
                        moves += 1
                if(total == 0):
                    total = moves
                else:
                    total = min(total,moves)
                    
            print('Case ' + str(casos) + ': ' + str(total))
            casos += 1
            
if __name__=='__main__':
    main()