# Felipe Menescal
# Online Judge
# 10035 Primary Arithmetic
import sys

def main():
	entrada = sys.stdin.read().splitlines()
	for linha in entrada:
		if(linha == '0 0'):
			break
		linha = linha.split()
		num1, num2 = linha[0], linha[1]
		if(len(num1) != len(num2)):
			if(max(len(num1),len(num2)) == len(num1)):
				num2 = '0'*(len(num1) - len(num2)) + num2
				carry = '0'*len(num1)
			else:
				num1 = '0'*(len(num2) - len(num1)) + num1
				carry = '0'*len(num2)
		else:	
			carry = '0'*len(num1)
		num1 = list(num1)
		num2 = list(num2)
		carry = list(carry)
		for i in range(len(carry) - 1, -1, -1):
			if((int(num1[i]) + int(num2[i]) + int(carry[i])) >= 10):
				carry[i-1] = '1'
		oco = carry.count('1')
		if(oco == 0):
			print('No carry operation.')
		if(oco == 1):
			print('1 carry operation.')
		if(oco > 1):
			print(str(oco) + ' carry operations.')
	
if __name__ == '__main__':
	main()