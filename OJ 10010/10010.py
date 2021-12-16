# Felipe Menescal
# Online Judge
# 10010 Where's Waldorf?
import sys
from collections import deque

def busca_leste(palavra, x, y, m):
	if(y == len(m[x]) -1):
		return False
	j = 0
	for i in range(y,len(m[x])):
		if(palavra[j] == m[x][i]):
			j = j + 1
			if(j == len(palavra)):
				return True
		else:
			return False

def busca_oeste(palavra, x, y, m):
	if(y == 0):
		return False
	j = 0
	for i in range(y,-1,-1):
		if(palavra[j] == m[x][i]):
			j = j + 1
			if(j == len(palavra)):
				return True
		else:
			return False

def busca_norte(palavra, x, y, m):
	if(x == 0):
		return False
	j = 0
	for i in range(x,-1,-1):
		if(palavra[j] == m[i][y]):
			j = j + 1
			if(j == len(palavra)):
				return True
		else:
			return False

def busca_sul(palavra, x, y, m):
	if(x == len(m) - 1):
		return False
	j = 0
	for i in range(x,len(m)):
		if(palavra[j] == m[i][y]):
			j = j + 1
			if(j == len(palavra)):
				return True
		else:
			return False

def busca_nordeste(palavra, x, y, m):
	if(y == len(m[x]) -1):
		return False
	if(x == 0):
		return False
	j = 0
	for i in range(x,-1,-1):
		if(palavra[j] == m[i][y]):
			j = j + 1
			y = y + 1
			if(j == len(palavra)):
				return True
		else:
			return False

def busca_noroeste(palavra, x, y, m):
	if(y == 0):
		return False
	if(x == 0):
		return False
	j = 0
	for i in range(x,-1,-1):
		if(palavra[j] == m[i][y]):
			j = j + 1
			y = y - 1
			if(j == len(palavra)):
				return True
		else:
			return False

def busca_sudeste(palavra, x, y, m):
	if(y == len(m[x]) -1):
		return False
	if(x == len(m) -1):
		return False
	j = 0
	for i in range(x,len(m)):
		if(palavra[j] == m[i][y]):
			j = j + 1
			y = y + 1
			if(j == len(palavra)):
				return True
		else:
			return False

def busca_sudoeste(palavra, x, y, m):
	if(y == 0):
		return False
	if(x == len(m) -1):
		return False
	j = 0
	for i in range(x,len(m)):
		if(palavra[j] == m[i][y]):
			j = j + 1
			y = y - 1
			if(j == len(palavra)):
				return True
		else:
			return False


def main():
	entrada = deque(sys.stdin.read().splitlines())
	casos = int(entrada.popleft())
	if(entrada[0] == ''):
		entrada.popleft()
	while(casos):
		dim = []
		m = []
		dim = entrada.popleft().split()
		m = [['' for x in range(1)] for y in range(int(dim[0]))]
		for i in range (len(m)):
			letras = entrada.popleft()
			letras = letras.casefold()
			m[i] = letras
		num_palavras = int(entrada.popleft())
		while(num_palavras):
			if(dim[1] == '1' and dim[0] == '1'):
				print('1 1')
				num_palavras = num_palavras - 1
				continue
			done = False
			palavra = entrada.popleft()
			palavra = palavra.casefold()
			for i in range(len(m)):
				if(not done):
					for j in range(len(m[i])):
						if(palavra[0] == m[i][j]):
							if(busca_leste(palavra, i, j, m)):
								print(str(i+1) + ' ' + str(j+1))
								done = True
								break
							if(busca_oeste(palavra,i,j,m)):
								print(str(i+1) + ' ' + str(j+1))
								done = True
								break
							if(busca_norte(palavra,i,j,m)):
								print(str(i+1) + ' ' + str(j+1))
								done = True
								break
							if(busca_sul(palavra,i,j,m)):
								print(str(i+1) + ' ' + str(j+1))
								done = True
								break
							if(busca_nordeste(palavra, i, j, m)):
								print(str(i+1) + ' ' + str(j+1))
								done = True
								break
							if(busca_noroeste(palavra,i,j,m)):
								print(str(i+1) + ' ' + str(j+1))
								done = True
								break
							if(busca_sudeste(palavra,i,j,m)):
								print(str(i+1) + ' ' + str(j+1))
								done = True
								break
							if(busca_sudoeste(palavra,i,j,m)):
								print(str(i+1) + ' ' + str(j+1))
								done = True
								break

						else:
							continue
				else:
					break
			num_palavras = num_palavras - 1
		casos = casos - 1
		print('')
		if(entrada):
			entrada.popleft()

if __name__ == '__main__':
	main()