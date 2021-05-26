import itertools
import time

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

			if linearray[0] == 'p':

				numeroVariables = int(linearray[2])
				numeroValuaciones = int(linearray[4])

				for i in range(numeroVariables):
					direcciones[i] = False

				readingInstructions = True

		else:
			if linearray[0] == '%':
				break

			setToAdd = set()

			for j in linearray:
				if j:
					if int(j) > 0:
						setToAdd.add((str(abs(int(j))),True))
					elif int(j) < 0:
						setToAdd.add((str(abs(int(j))),False))

  

			valuaciones.append(setToAdd)

	# print(f"Numero de variables: {numeroVariables}")
	# print(f"Numero de valuaciones: {numeroValuaciones}")

	return [numeroVariables, valuaciones]


def bruteForce(Formula):
	# Formula de la siguiente manera: [Numero de variables , [Clauslas]]

	numberOfLiterals = Formula[0]
	
	direcciones = Formula[1]

	literals = set()

	for conjuncion in direcciones:
		for disjuncion in conjuncion:
			literals.add(disjuncion[0])


	iterating = list(itertools.product([True, False], repeat = numberOfLiterals))

	for combinacion in iterating:
		a = set(zip(literals, combinacion))

		if all([bool(disjuncion.intersection(a)) for disjuncion in direcciones]):
			#return True, a
			return 1
	
	return 0


def __select_literal(cnf):
    for c in cnf:
        for literal in c:
            return literal[0]

def dpll_wrap(Formula):
	val = my_dpll(Formula[1])
	if val[0]:
		return 1
	return 0

# Implementacion de DPLL basada en https://davefernig.com/2018/05/07/solving-sat-in-python/
def my_dpll(direcciones, assignments={}):
	

	if len(direcciones) == 0:
		return True, assignments

	if any([len(conjuncion)==0 for conjuncion in direcciones]):
		return False, None

	variable = __select_literal(direcciones)

	new_cnf = [c for c in direcciones if (variable, True) not in c]
	new_cnf = [c.difference({(variable, False)}) for c in new_cnf]
	sat, vals = my_dpll(new_cnf, {**assignments, **{variable: True}})
	if sat:
		return sat, vals

	new_cnf = [c for c in direcciones if (variable, False) not in c]
	new_cnf = [c.difference({(variable, True)}) for c in new_cnf]
	sat, vals = my_dpll(new_cnf, {**assignments, **{variable: False}})

	if sat:
		return sat, vals
 
	return False, None


def individualTest(filename, brute=False):

	testingParse = ParserDimacs(filename)

	start_dpll = time.time()
	valdpll = dpll_wrap(testingParse)
	print(f"Valor test DPLL: {valdpll}")
	end_dpll = time.time()

	print(f"TIEMPO DPLL: {(end_dpll-start_dpll)}")

	if brute:
		start_brute = time.time()
		valfb = bruteForce(testingParse)
		print(f"Valor test FB: {valfb}")
		end_brute = time.time()
		print(f"TIEMPO FUERZA BRUTA: {(end_brute-start_brute)}")

	print("")

def complete_Testing():

	print("")
	print("Testeando satisfacibles 20\n")


	for i in range(1,21):
		file = f"20_sat/uf20-0{i}.cnf"
		print(f"	Test {i}, archivo: uf20-0{i}.cnf")
		individualTest(file, brute=True)

	print("Testeando insatisfacibles 50\n")

	for i in range(1,11):
		file = f"50_unsat/uuf50-0{i}.cnf"
		print(f"	Test {i}, archivo: uuf50-0{i}.cnf")
		individualTest(file, brute=False)


	print("")
	print("Testeando satisfacibles 50\n")

	for i in range(1,11):
		file = f"50_sat/uf50-0{i}.cnf"
		print(f"	Test {i}, archivo: uf50-0{i}.cnf")
		individualTest(file, brute=False)

complete_Testing()

# exampleCNF = [{("p", False), ("q", False)}, {("p", True), ("r", False)}]
# print(example_brute_force(exampleCNF))
# print(bruteForce([3, exampleCNF]))
