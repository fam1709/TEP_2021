# Felipe Menescal
# Online Judge
# 10041 Vito's Family
import sys
from collections import deque
from statistics import median

def main():
	entrada = deque(sys.stdin.read().splitlines())
	casos = int(entrada.popleft())
	for i in range(casos):
		caso = deque(entrada.popleft().split())
		parentes = int(caso.popleft())
		soma_min = 0
		caso = map(int,caso)
		caso = sorted(caso)
		casa_vito = int(median(caso))
		for j in range(len(caso)):
			soma_min = soma_min + abs(casa_vito - caso[j])
		print(soma_min)


if __name__ == '__main__':
	main()