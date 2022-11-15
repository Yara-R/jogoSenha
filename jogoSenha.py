import os
os.system("cls")

import random
import time
def jogo():
	nums = list(range(10))
	random.shuffle(nums)
	n1, n2, n3, n4 = nums[:4]

	password = str(n1) + str(n2) + str(n3) + str(n4)
	par = 0

	if n1 % 2 == 0:
		par += 1

	if n2 % 2 == 0:
		par += 1

	if n3 % 2 == 0:
		par += 1

	if n4 % 2 == 0:
		par += 1

	print("\nVocê conseguiu acessar o controle da bomba!\nPara desarma-la, digite a senha de 4 dígitos corretamente.\nVocê tem 60 segundos!")
	print(f"Dica: A senha possui {par} numero(s) par(es)\n")

	while True:
		guess = input("Digite uma senha de 4 digitos: ")
		presente = 0
		certo = 0

		nums = [n1, n2, n3, n4]

		if str(n1) in guess:
			presente += 1
		if str(n2) in guess:
			presente += 1
		if str(n3) in guess:
			presente += 1
		if str(n4) in guess:
			presente += 1

		if(guess[0]==password[0]):
			print("\nO primeiro número está certo!")
		if(guess[1]==password[1]):
			print("\nO segundo número está certo!")
		if(guess[2]==password[2]):
			print("\nO terceiro número está certo!")
		if(guess[3]==password[3]):
			print("\nO quarto número está certo!")

		if presente == 4:
			print("\nParabéns! Você conseguiu desmontar a bomba\n")
			a='a'
			return(a)

		elif presente == 4 :
			print(f"\nTodos os numeros fazem parte da senha.\n")

		else:
			print(f"\n{presente} números fazem parte da senha.")
