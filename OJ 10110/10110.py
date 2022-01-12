# Felipe Menescal
# Online Judge
# 10110 Light, More Light - Square Numbers
import sys, math

def main():
    entrada = sys.stdin.read().splitlines()
    for linha in entrada:
        if(linha == '0'):
            break
        ans = math.sqrt(int(linha))
        if(ans.is_integer()):
            print('yes')
        else:
            print('no')

if __name__=='__main__':
    main()