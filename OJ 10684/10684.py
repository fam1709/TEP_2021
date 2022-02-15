# Felipe Menescal
# Online Judge
# 10684 The Jackpot
import sys

def main():
    entrada = sys.stdin.read().splitlines()
    seq_len = 0
    for linha in entrada:
        if(linha == '' or linha == ' '):
            continue
        if(not seq_len):
            seq_len = int(linha)
            cum_sum = []
            bets = []
        else:
            linha = linha.split()
            seq_len -= len(linha)
            for l in linha:
                bets.append(int(l))
            if(not seq_len):
                cum_sum.append(bets[0])
                for i in range(1,len(bets)):
                    cum_sum.append(max(cum_sum[i-1] + bets[i], bets[i]))
                res = max(cum_sum)
                if(res <= 0):
                    print('Losing streak.')
                else:
                    print('The maximum winning streak is ' + str(res) + '.')



if __name__=='__main__':
    main()