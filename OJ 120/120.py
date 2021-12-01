# Felipe Menescal
# Online Judge
# 120 Stack of FlapJacks

import sys

def main():
	entrada = sys.stdin.read().splitlines()
	for linha in entrada:
		pilha_original = []
		flips = ''
		print(linha)
		pilha_original = linha.split()
		for i in range(len(pilha_original)):
			pilha_original[i] = int(pilha_original[i])
		if(pilha_original == sorted(pilha_original)):
				flips = flips + '0'
				print(flips)
				continue
		pilha_ordem = sorted(pilha_original)
		for i in range(len(pilha_ordem[::-1])):
			if(pilha_original == pilha_ordem):
				flips = flips + '0'
				break
			elif(pilha_ordem[::-1][i] == pilha_original[(i + 1)*-1]):
				continue
			elif(pilha_ordem[::-1][i] == pilha_original[0]):
				flips = flips + str(i+1) + ' '
				rev = pilha_original[(i+1)*-1::-1]
				for j in range(len(rev)):
					pilha_original[j] = rev[j]
			else:
				pos = (pilha_original[::-1].index(pilha_ordem[::-1][i]) + 1) * -1
				flips = flips + str(pos * -1)  + ' '
				rev = pilha_original[pos::-1]
				for j in range(len(rev)):
					pilha_original[j] = rev[j]
				flips = flips + str(i+1) + ' '
				rev = pilha_original[(i+1)*-1::-1]
				for j in range(len(rev)):
					pilha_original[j] = rev[j]
		print(flips)

if __name__ == '__main__':
	main()
	print('')