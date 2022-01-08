# Felipe Menescal
# Online Judge
# 10213 How Many Pieces of Land? - Moser's Circle
import sys
import operator as op
from functools import reduce

def comb(n,k):
	if (k>n):
		return 0
	k = min(k,n-k)
	num = reduce(op.mul, range(n, n-k, -1), 1)
	dem = reduce(op.mul, range(1, k+1), 1)
	return  num // dem

def main():
	entrada = sys.stdin.read().splitlines()
	entrada.pop(0)
	for linha in entrada:
		res = comb(int(linha),4) + comb(int(linha),2) + 1
		print(str(res))

if __name__ == '__main__':
	main()