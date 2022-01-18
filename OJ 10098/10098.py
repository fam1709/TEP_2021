# Felipe Menescal
# Online Judge
# 10098 Generating Fast, Sorted Permutations - Lexicographic Permutations Dijkstra's
import sys

def lex_dijks(s,d):
    print(''.join(s))
    d[''.join(s)] = 1
    i = len(s) - 1
    while(s[i - 1] >= s[i]):
        i -= 1
        if( i == len(s)*-1):
            return
    j = len(s)
    while(s[j-1] <= s[i-1]):
        j -= 1

    s[i-1], s[j-1] = s[j-1], s[i-1]

    i += 1
    j = len(s)

    while(i < j):
        s[i-1], s[j-1] = s[j-1], s[i-1]
        i += 1
        j -= 1



def main():
    entrada = sys.stdin.read().splitlines()
    entrada.pop(0)
    for linha in entrada:
        permut = {}
        linha = sorted(linha)
        while((''.join(linha)) not in permut):
            lex_dijks(linha, permut)
        print('')
if __name__=='__main__':
    main()