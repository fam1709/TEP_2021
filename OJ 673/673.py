# Felipe Menescal
# Online Judge
# 673 Parentheses Balance 
# Checks if a string consisting of () and [] is balanced, for every open ( or [ there is a closed ) and ] 

import sys

def main():
	entrada = sys.stdin.read().splitlines()
	entrada.pop(0)
	for linha in entrada:
		pilha = []
		especial = False 
		for letra in linha:
			if(letra in ['(','[']):
				pilha.append(letra)
			else:
				if(not pilha):
					especial = True
					break
				elem = pilha.pop()
				if(elem == '('):
					if(letra != ')'):
						especial = True
						break
				elif(elem == '['):
					if(letra != ']'):
						especial = True
						break
		if(pilha):
			print('No')
		elif(especial):
			print('No')
		else:
			print('Yes')

if __name__ == '__main__':
	main()