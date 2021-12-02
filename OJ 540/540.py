# Felipe Menescal
# Online Judge
# 540 Team Queue
# Simulation of a Team Queue
import sys

def main():
	entrada = sys.stdin.read().splitlines()
	casos = 1
	while(True):
		fila = []
		num_times = int(entrada.pop(0))
		if(num_times == 0):
			break
		dict_times = {}
		lista_chaves = []
		for i in range(num_times):
			dict_times[i] = entrada.pop(0).split()[1:]
		print('Scenario #' + str(casos))
		for linha in entrada:
			if(linha == 'STOP'):
				entrada = entrada[entrada.index(linha) + 1:len(entrada)]
				casos = casos + 1
				print('')
				break
			if('ENQUEUE' in linha):
				elem = linha.split()[1]
				for k,v in dict_times.items():
					if elem in v:
						chave_elem = k
						break
				if not fila:
					fila.append(elem)
					lista_chaves.append(chave_elem)
				else:
					if chave_elem in lista_chaves:
						pos = lista_chaves[::-1].index(chave_elem)
						if pos == 0:
							fila.append(elem)
							lista_chaves.append(chave_elem)
						else:
							nova_pos = len(lista_chaves) - pos
							fila.insert(nova_pos,elem)
							lista_chaves.insert(nova_pos,chave_elem)
					else:
						lista_chaves.append(chave_elem)
						fila.append(elem)
			if('DEQUEUE' in linha):
				head = fila.pop(0)
				lista_chaves.pop(0)
				print(head)

if __name__ == '__main__':
	main()
	print('')