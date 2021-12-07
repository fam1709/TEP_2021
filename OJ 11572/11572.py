# Felipe Menescal
# Online Judge
# 11572 Unique Snowflakes
import sys
from collections import deque

def main():
	entrada = deque(sys.stdin.read().splitlines())
	casos = int(entrada.popleft())
	for i in range(casos):
		num_flocos = int(entrada.popleft())
		if(num_flocos == 1):
			print('1')
			entrada.popleft()
			continue
		pos_flocos = {}
		dist = 0
		dupli = 0
		cnt = 0
		for j in range(num_flocos):
			floco = int(entrada.popleft())
			if not pos_flocos:
				pos_flocos[floco] = j
				cnt = cnt + 1
			else:
				if floco in pos_flocos:
					idx = pos_flocos.get(floco)
					dupli = max(dupli,idx)
					cnt = j - dupli - 1
				cnt = cnt + 1
				pos_flocos[floco] = j
				dist = max(dist,cnt)
		print(dist)
if __name__ == '__main__':
	main()