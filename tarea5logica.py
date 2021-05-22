def notFunction(boolean):
	if boolean:
		return False
	else:
		return True

def ParserDimacs(filename):
	
	file1 = open(filename, 'r')
	Lines = file1.readlines()

	readingInstructions = False

	numeroVariables = 0
	numeroValuaciones = 0

	direcciones = {}
	valuaciones = {}

	counter = 0

	# Strips the newline character
	for line in Lines:
		linearray = line.strip("\n")
		linearray = linearray.split(" ")

		if not(readingInstructions):

			if linearray[0] == 'c':
				print("Linea de comentario")
				print(line)

			elif linearray[0] == 'p':
				print("inicio de instrucciones")
				print(line)

				numeroVariables = int(linearray[2])
				numeroValuaciones = int(linearray[4])

				for i in numeroVariables:
					variables[i] = False

				readingInstructions = True

		else:
			listToAdd = []

			for j in linearray:
				numbah = int(j)
				if numbah < 0:

	print(f"Numero de variables: {numeroVariables}")
	print(f"Numero de valuaciones: {numeroValuaciones}")

ParserDimacs("uf20-01.cnf")