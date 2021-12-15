# Felipe Menescal
# Online Judge
# 10305 Ordering Tasks - Topo. Sort
import sys
from collections import deque


def main():
	entrada = deque(sys.stdin.read().splitlines())
	while(True):
		tarefas,arestas = entrada.popleft().split()
		vertices = {}
		S = deque()
		L = ''
		if(tarefas == '0' and arestas == '0'):
			break
		else:
			for i in range(int(tarefas)):
				vertices[i+1] = []
			for i in range(int(arestas)):
				out,inc = entrada.popleft().split()
				vertices[int(inc)].append(int(out))
			for k,v in vertices.items():
				if(v == []):
					S.append(str(k))
			while(S):
				n = S.popleft()
				L = L + n + ' '
				for k,v in vertices.items():
					if(v == []):
						continue
					elif(int(n) in v):
						vertices[k].remove(int(n))
						if(vertices[k] == []):
							S.append(str(k))
			print(L)




if __name__ == '__main__':
	main()