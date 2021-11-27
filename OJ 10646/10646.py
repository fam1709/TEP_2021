# Felipe Menescal
# Online Judge
# 10646 What is the Card?
# Value of card equals value of the card face if face [2,9], otherwise value is 10
# Pile of 52 cards with faces down. Take the top 25 cards.
# Set Y = 0 and execute this 3 steps 3 times
#	1 - Take the top card from the 25 pile and determine its value
#	2 - Let the card value be X. Add X to Y
#	3 - Put this card and the top (10 - X) cards of the pile away
import sys

def main():
	entrada = sys.stdin.read().splitlines()
	entrada.pop(0)
	pilha_52 = []
	casos = 1
	for linha in entrada:
		pilha_52 = linha.split()
		i = 0
		pilha_25 = []
		while(i < 25):
			pilha_25.append(pilha_52.pop())
			i = i + 1
		Y = 0
		i = 0
		while(i < 3):
			carta = ''
			carta = pilha_52.pop()
			if('A' in carta or 'K' in carta or 'Q' in carta or 'J' in carta or 'T' in carta):
				X = 10
				Y = Y + X
			elif(carta[0].isdigit()):
				X = int(carta[0])
				Y = Y + X
			j = 0
			while(j < (10 - X)):
				pilha_52.pop()
				j = j + 1
			i = i + 1
		pilha_25.reverse()
		for carta in pilha_25:
			pilha_52.append(carta)
		print('Case ' + str(casos) +': '+ pilha_52[Y-1])
		casos = casos + 1

if __name__ == '__main__':
	main()
	print('\n')
