# Felipe Menescal
# Online Judge
# 11111 Generalized Matrioshkas

import sys

def main():
	entrada = sys.stdin.read().splitlines()
	for linha in entrada:
		if(linha == ''):
			print(':-) Matrioshka!')
			continue
		toys = linha.split()
		if(len(toys) == 1):
			print(':-( Try again.')
			continue
		pilha_parse = []
		fail = False
		for t in toys:
			t = int(t)
			if t < 0:
				pilha_parse.append(t)
			else:
				num_pops = 0
				j = 0
				elem = pilha_parse.pop()
				while(j < t):
					if elem == t*(-1):
						pilha_parse.append(t)
						break
					elif elem < 0:
						fail = True
						break
					else:
						num_pops = num_pops + elem
						if num_pops >= t:
							fail = True
							break
					j = j + 1
					elem = pilha_parse.pop()
			if(fail):
				break
		if not fail:
			for elem in pilha_parse:
				if elem < 0:
					fail = True
					break
			if not fail:
				print(':-) Matrioshka!')
			else:
				print(':-( Try again.')
		else:
			print(':-( Try again.')
		
if __name__ == '__main__':
	main()