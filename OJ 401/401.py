# Felipe Menescal
# Online Judge
# 401 Palindromes 
# Checks if a string is a palindrome, a mirrored string, both or none

import sys

def main():
	entrada = sys.stdin.read().splitlines()
	char = 'AEHIJLMOSTUVWXYZ12358'
	char_espelho = 'A3HILJMO2TUVWXY51SEZ8'
	tabela = dict(zip(char,char_espelho))
	for linha in entrada:
		count = 0
		for letra in linha:
			try:
				if(tabela[letra] == linha[::-1][count]):
					count = count + 1
			except KeyError:
				break
		if(count == len(linha) and linha == linha[::-1]):
			print(linha + ' -- is a mirrored palindrome.\n')
		elif (linha == linha[::-1]):
			print(linha + ' -- is a regular palindrome.\n')
		elif(count == len(linha)):
			print(linha + ' -- is a mirrored string.\n')
		else:
			print(linha + ' -- is not a palindrome.\n')
	
if __name__ == '__main__':
	main()