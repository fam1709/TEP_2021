# Felipe Menescal
# Online Judge
# 10377 Maze Traversal
import sys

def main():
    entrada = sys.stdin.read().splitlines()
    entrada.pop(0)
    entrada.pop(0)
    aux = 0
    comandos = ''
    direcoes = 'NESW'
    orientacao = 0
    ori_robo = 'N'
    for linha in entrada:
        if(linha == ''):
            print('')
            continue
        
        elif(aux == -1):
            if(linha.split()[0].isdigit()):
                linha = linha.split()
                x, y = int(linha[0]) - 1, int(linha[1]) - 1
               
            else:
                comandos += linha
                if('Q' in linha):
                    for c in comandos:
                        if(c == ' '):
                            continue
                        elif(c == 'L'):
                            orientacao -= 1
                            ori_robo = direcoes[orientacao%4]
                        elif(c == 'R'):
                            orientacao += 1
                            ori_robo = direcoes[orientacao%4]
                        elif(c == 'F'):
                            if(ori_robo == 'N'):
                                if(labir[x-1][y] == ' '):
                                    x = x - 1
                            elif(ori_robo == 'S'):
                                if(labir[x+1][y] == ' '):
                                    x = x + 1
                            elif(ori_robo == 'E'):
                                if(labir[x][y+1] == ' '):
                                    y = y + 1
                            elif(ori_robo == 'W'):
                                if(labir[x][y-1] == ' '):
                                    y = y - 1
                    print(x+1,y+1,ori_robo)
                    aux = 0
                    comandos = ''
                    ori_robo = 'N'
                    orientacao = 0
        elif(aux == 0):
            linha = linha.split()
            lin, col = int(linha[0]), int(linha[1])
            labir = []
            aux = lin
        else:
            labir.append(linha)
            aux -= 1
            if(not aux):
                aux = -1
                continue

    
if __name__=='__main__':
    main()