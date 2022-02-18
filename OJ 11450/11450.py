# Felipe Menescal
# Online Judge
# 11450 Wedding Shopping
import sys

def din_prog(money_total,money_left, idx, memoir, items, precos):
    if(money_left < 0):
        return -1
    if(idx == items):
        return money_total - money_left
    if((money_left,idx) in memoir):
        return memoir[(money_left,idx)]
    res = -1
    for i in range(len(precos[idx])):
        res = max(din_prog(money_total,money_left - int(precos[idx][i]), idx + 1, memoir, items, precos), res)

    memoir[(money_left,idx)] = res
    return res


def main():
    entrada = sys.stdin.read().splitlines()
    entrada.pop(0)
    items = 0
    for linha in entrada:
        if(not items):
            linha = linha.split()
            money, items = int(linha[0]), int(linha[1])
            precos = [[]]*items
            j = 0
        else:
            linha = linha.split()[1:]
            precos[j] = linha
            j += 1
            if(items - j == 0):
                memoir = {}
                max_mny = din_prog(money,money,0,memoir,items,precos)
                if(max_mny < 0):
                    print('no solution')
                else:
                    print(max_mny)
                items = 0


if __name__=='__main__':
    main()