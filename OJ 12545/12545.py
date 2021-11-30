# Felipe Menescal
# Online Judge
# 12545 Bits Equalizer
# Turns string S into string T with the least amount of moves
# 0 can become 1
# ? can become 0 or 1
# swap any two chars
import sys

def main():
	entrada = sys.stdin.read().splitlines()
	casos = int(entrada.pop(0))
	for j in range(casos):
		movimentos = 0
		S = ''
		T = ''
		pilha_zeros = []
		pilha_ums = []
		S = entrada.pop(0)
		T = entrada.pop(0)
		if(S.count('1') > T.count('1')):
			print('Case ' + str(j+1) + ': -1')
		if(S.count('1') == T.count('1')):
			S = list(S)
			T = list(T)
			for i in range(len(S)):
				if(S[i] == '?'):
					S[i] = '0'
					movimentos = movimentos + 1
					if(T[i] == '1'):
						pilha_zeros.append(i)
				elif(S[i] == '0' and T[i] == '1'):
					pilha_zeros.append(i)
				elif(S[i] == '1' and T[i] == '0'):
					pilha_ums.append(i)
			while(len(pilha_zeros) > len(pilha_ums)):
				pos = pilha_zeros.pop()
				S[pos] = '1'
				movimentos = movimentos + 1
			while(len(pilha_zeros) > 0):
				pos_0 = pilha_zeros.pop()
				pos_1 = pilha_ums.pop()
				aux = S[pos_0]
				S[pos_0] = S[pos_1]
				S[pos_1] = aux
				movimentos = movimentos + 1
			if(S == T):
				print('Case ' + str(j+1) + ': '+ str(movimentos))
		if(S.count('1') < T.count('1')):
			S = list(S)
			T = list(T)
			for i in range(len(S)):
				if(S[i] == '?' and T[i] == '1'):
					if(S.count('1') >= T.count('1')):
						S[i] = '0'
						pilha_zeros.append(i)
						movimentos = movimentos + 1
					else:
						S[i] = '1'
						movimentos = movimentos + 1
				elif(S[i] == '?' and T[i] == '0'):
					S[i] = '0'
					movimentos = movimentos + 1
				elif(S[i] == '0' and T[i] == '1'):
					pilha_zeros.append(i)
				elif(S[i] == '1' and T[i] == '0'):
					pilha_ums.append(i)
			while(len(pilha_zeros) > len(pilha_ums)):
				pos = pilha_zeros.pop()
				S[pos] = '1'
				movimentos = movimentos + 1
			while(len(pilha_zeros) > 0):
				pos_0 = pilha_zeros.pop()
				pos_1 = pilha_ums.pop()
				aux = S[pos_0]
				S[pos_0] = S[pos_1]
				S[pos_1] = aux
				movimentos = movimentos + 1
			if(S == T):
				print('Case ' + str(j+1) + ': '+ str(movimentos))


if __name__ == '__main__':
	main()