# Felipe Menescal
# Online Judge
# 130 Roman Roulette 

import sys

def main():
	entrada = sys.stdin.read().splitlines()
	for linha in entrada:
		n,k = linha.split()
		n = int(n)
		k = int(k)
		circ = []
		num_mortos = 0
		if(n == 0 and k == 0):
			break
		for i in range(n):
			circ.append(i+1)
		if(len(circ) == 1):
			print(circ[0])
			continue
		pos_morto = (k - 1)%n
		while(True):
			circ[pos_morto] = -1
			num_mortos = num_mortos + 1
			if((n - num_mortos) == 1):
				circ.remove(-1)
				if(circ[0] == 1):
					print(1)
					break
				print(n - circ[0] + 2)
				break
			indx_coveiro = (pos_morto + (k-1))% (n - num_mortos)
			if(indx_coveiro >= pos_morto):
				circ.remove(-1)
				coveiro = circ.pop(indx_coveiro)
				circ.insert(pos_morto,coveiro)
				indx_nova_coveiro = circ.index(coveiro)
			else:
				coveiro = circ[indx_coveiro]
				circ[indx_coveiro],circ[pos_morto] = circ[pos_morto],circ[indx_coveiro]
				circ.remove(-1)
				indx_nova_coveiro = circ.index(coveiro)
			pos_morto = (indx_nova_coveiro + k)%(n-num_mortos) 


if __name__ == '__main__':
	main()