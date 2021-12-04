# Felipe Menescal
# Online Judge
# 514 Rails
import sys
from collections import deque

def main():
	entrada = sys.stdin.read().splitlines()
	trem_A = deque()
	zeros = 0 # uma forma de escapar do presentation error neste problema
	for linha in entrada:
		if(linha.isdigit()):
			if(linha == '0'):
				zeros = zeros + 1
				if(zeros == 2):
					break
				print('')
				continue
			else:
				zeros = 0
				trem_A = deque()
				for i in range(int(linha)):
					trem_A.append(i+1)
				continue
		aux = trem_A.copy()
		formacao = linha.split()
		estacao = []
		for i in range(len(formacao)):
			if(int(formacao[i]) in estacao):
				if(int(formacao[i]) == estacao[-1]):
					estacao.pop()
					if (not estacao):
						print('Yes')
						break
					continue
				else:
					print('No')
					break
			if(not aux and not estacao):
				print('Yes')
			idx = aux.index(int(formacao[i]))
			if(idx == 0):
				aux.popleft()
				if(not aux and not estacao):
					print('Yes')
					break
			else:
				while(idx > 0):
					estacao.append(aux.popleft())
					idx = idx - 1
				aux.remove(int(formacao[i]))


	
if __name__ == '__main__':
	main()