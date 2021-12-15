# Felipe Menescal
# Online Judge
# 200 Rare Oder - Topo. Sort
import sys
from collections import deque
from graphlib import TopologicalSorter

def main():
	entrada = deque(sys.stdin.read().splitlines())
	ord_string = deque()
	ts = TopologicalSorter()
	for linha in entrada:
		if(linha != '#'):
			ord_string.append(linha)
			continue
		else:
			for i in range(len(ord_string) - 1):
				s1 = ord_string[i]
				s2 = ord_string[i+1]
				tam = len(min(s1,s2))
				j = 0
				while(j < tam):
					if(s1[j] != s2[j]):
						ts.add(s2[j],s1[j])
						break
					j = j + 1
			res = [*ts.static_order()]
			out = ''
			for i in range(len(res)):
				out = out + res[i]
			print(out)
			ord_string = deque()
			ts = TopologicalSorter()

if __name__ == '__main__':
	main()