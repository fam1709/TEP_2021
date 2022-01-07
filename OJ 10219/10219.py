# Felipe Menescal
# Online Judge
# 10219 Find the Ways!
import sys
from math import floor, log
import operator as op
from functools import reduce

def main():
	entrada = sys.stdin.read().splitlines()
	for linha in entrada:
		linha = linha.split()
		n,k = int(linha[0]), int(linha[1])
		k = min(k,n-k)
		num = reduce(op.mul, range(n, n-k, -1), 1)
		dem = reduce(op.mul, range(1, k+1), 1)
		res = num // dem
		res = str(floor(log(res,10)) + 1)
		print(res)
		


if __name__ == '__main__':
	main()