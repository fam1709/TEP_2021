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
		for i in range(num_times):
			dict_times[i] = entrada.pop(0)
		print('Scenario #' + str(casos))
		for linha in entrada:
			if(linha == 'STOP'):
				a = entrada.index(linha)
				entrada = entrada[entrada.index(linha) + 1:len(entrada)]
				casos = casos + 1
				print('')
				break
			if('ENQUEUE' in linha):
				elem = linha.split()[1]
				if not fila:
					fila.append(elem)
				else:
					pos_ult_membro = 0
					for j in range(len(fila)):
						possivel_membro = fila[j]
						for k in range(len(dict_times)):
							if (elem in list(dict_times.items())[k][1].split()[1:] and possivel_membro in list(dict_times.items())[k][1].split()[1:]):
								pos_ult_membro = j + 1 
								break
					if(pos_ult_membro  == 0):
						fila.append(elem)
					else:
						fila.insert(pos_ult_membro, elem)
			if('DEQUEUE' in linha):
				head = fila.pop(0)
				print(head)

if __name__ == '__main__':
	main()
	print('')