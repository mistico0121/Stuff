import itertools

def notFunction(boolean):
	if boolean:
		return False
	else:
		return True

def orFunction(a, b):
	return (a or b)

def ParserDimacs(filename):
	
	file1 = open(filename, 'r')
	Lines = file1.readlines()

	readingInstructions = False

	numeroVariables = 0
	numeroValuaciones = 0

	direcciones = {}
	valuaciones = []

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

				for i in range(numeroVariables):
					direcciones[i] = False

				readingInstructions = True

		else:
			if linearray[0] == '%':
				break

			listToAdd = []

			for j in linearray:
				if j:
					listToAdd.append(int(j))


			valuaciones.append(listToAdd)

	print(f"Numero de variables: {numeroVariables}")
	print(f"Numero de valuaciones: {numeroValuaciones}")

	print(valuaciones)

	l = [False, True]
	iterating = list(itertools.product(l, repeat = numeroValuaciones))



	for combination in iterating:
		counter = 1
		for value in combination:
			direcciones[counter] = value
			counter += 1

		boolProp = True

		for proposition in valuaciones:
			toEvaluate = []
			for value in proposition:
				if value>0:
					toEvaluate.append(direcciones(value))
				elif value<0:
					toEvaluate.append(notFunction(direcciones(value)))

			boolProp = reduce(orFunction, toEvaluate)

			if not boolProp:
				break

		if counter == numeroValuaciones:
			return True

	return False




ParserDimacs("uf20-01.cnf")