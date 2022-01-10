# Felipe Menescal
# Online Judge
# 11955 Binomial Theorem
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
	caso = 1
	for linha in entrada:
		a, b, pot = linha[1:linha.index('+')], linha[linha.index('+')+1:linha.index(')')], linha[linha.index('^') + 1:]
		if(pot == '1'):
			print('Case ' + str(caso) + ': ' + a + '+' + b)
			caso = caso + 1
			continue
		res = ''
		for i in range(int(pot) + 1):
			aux = str(comb(int(pot), i))
			if(aux == '1'):
				coef = ''
			else:
				coef = aux + '*'
			expA = a + '^' + str(int(pot) - i)
			if(int(pot) - i == 0):
				expA = ''
			if(int(pot) - i == 1):
				expA = a
			expB = '*' + b + '^' + str(i)
			if(i == 0 ):
				expB = ''
			if(i == 1 ):
				expB = '*' + b
			if(i == int(pot)):
				expB = b + '^' + str(i)
			res = res + coef + expA + expB + '+'
		print('Case ' + str(caso) + ': ' + res[:-1])
		caso = caso + 1

if __name__ == '__main__':
	main()