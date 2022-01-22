# Felipe Menescal
# Online Judge
# 10576 Y2K Accounting Bug
import sys

def main():
    entrada = sys.stdin.read().splitlines()
    meses = []
    for linha in entrada:
        validos = [True]*12
        linha = linha.split()
        s, d = int(linha[0]), int(linha[1]) * -1
        meses = [d]*12
        for i in range(8):
            for j in range(5):
                if(validos[j+i]):
                    meses[j+i] = s
                if(sum(meses[i:i+5]) > 0):
                    meses[j+i] = d
                    validos[j+i] = False
        print(sum(meses) if sum(meses) > 0 else 'Deficit')
                    
if __name__=='__main__':
    main()