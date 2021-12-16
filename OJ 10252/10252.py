# Felipe Menescal
# Online Judge
# 10252 Common Permutation
import sys
from collections import deque

def main():
	entrada = deque(sys.stdin.read().splitlines())
	alpha ='abcdefghijklmnopqrstuvwxyz'
	while(entrada):
		list_strings = []
		for i in range(2):
			list_strings.append(entrada.popleft())
		s1, s2 = list_strings[0], list_strings[1]
		saida = ''
		if(s1 == '' or s2 == ''):
			print('')
		else:
			for letra in alpha:
				cnt = 0
				if(letra in s1 and letra in s2):
					cnt = min(s1.count(letra), s2.count(letra))
					saida = saida + letra*cnt
			saida = sorted(saida)
			s = ''
			for i in saida:
				s = s + i
			print(s)



if __name__ == '__main__':
	main()