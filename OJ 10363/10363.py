# Felipe Menescal
# Online Judge
# 10363 Tic Tac Toe
import sys

def ver_colunas(tab,jogador):
    for i in range(3):
        coluna = [tab[k][i] for k in range(3)]
        if(coluna.count(jogador) == 3):
            return True
    return False

def ver_diag(tab,jogador):
        diag1 = [tab[k][k] for k in range(3)]
        if(diag1.count(jogador) == 3):
            return True
        diag2 = [tab[k][2-k] for k in range(3)]
        if(diag2.count(jogador) == 3):
            return True
        return False
def main():
    entrada = sys.stdin.read().splitlines()
    entrada.pop(0)
    nmr_x = 0
    nmr_o = 0
    i = 0
    tab = [[0]*3]*3
    ganhou_x = False
    ganhou_o = False
    for linha in entrada:
        if(linha == '' or linha == ' '):
            nmr_x = 0
            nmr_o = 0
            i = 0
            ganhou_x = False
            ganhou_o = False
            continue
        linha = list(linha)
        tab[i] = linha
        nmr_x += linha.count('X')
        if(linha.count('X') == 3):
            ganhou_x = True
        nmr_o += linha.count('O')
        if(linha.count('O') == 3):
            ganhou_o = True
        i += 1
        if(i == 3):
            if(ver_colunas(tab,'X')):
                ganhou_x = True
            if(ver_colunas(tab,'O')):
                ganhou_o = True
            if(ver_diag(tab,'X')):
                ganhou_x = True
            if(ver_diag(tab,'O')):
                ganhou_o = True

            if(nmr_o > nmr_x):
                print('no')
                continue
            elif(nmr_x > nmr_o + 1):
                print('no')
                continue
            elif(ganhou_o and nmr_o == nmr_x and not ganhou_x):
                print('yes')
                continue
            elif(ganhou_x and nmr_x > nmr_o and not ganhou_o):
                print('yes')
                continue
            elif(not ganhou_x and not ganhou_o and nmr_x >= nmr_o):
                print('yes')
                continue
            else:
                print('no')
                continue
            
if __name__=='__main__':
    main()