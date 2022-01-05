# Felipe Menescal
# Online Judge
# 10018 Reverse and Add
import sys
from collections import deque

def main():
	entrada = deque(sys.stdin.read().splitlines())
	casos = int(entrada.popleft())
	for i in range(casos):
		numero = entrada.popleft()
		rep = 0
		while(True):
			numero_rev = numero[::-1]
			soma = str(int(numero) + int(numero_rev))
			rep = rep + 1
			if(soma == soma[::-1]):
				break
			numero = soma
		print(str(rep) + ' ' + soma)


if __name__ == '__main__':
	main()