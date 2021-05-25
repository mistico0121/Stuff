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
			print (disjuncion)
			return True, a
	
	return False


def __select_literal(cnf):
    for c in cnf:
        for literal in c:
            return literal[0]
 
def dpll(cnf, assignments={}):
 
    if len(cnf) == 0:
        return True, assignments
 
    if any([len(c)==0 for c in cnf]):
        return False, None
 
    l = __select_literal(cnf)
 
    new_cnf = [c for c in cnf if (l, True) not in c]
    new_cnf = [c.difference({(l, False)}) for c in new_cnf]
    sat, vals = dpll(new_cnf, {**assignments, **{l: True}})
    if sat:
        return sat, vals
 
    new_cnf = [c for c in cnf if (l, False) not in c]
    new_cnf = [c.difference({(l, True)}) for c in new_cnf]
    sat, vals = dpll(new_cnf, {**assignments, **{l: False}})
    if sat:
        return sat, vals
 
    return False, None



def example_brute_force(cnf):

	print(cnf)
	literals = set()
	for conj in cnf:
		for disj in conj:
			literals.add(disj[0])


	literals = list(literals)
	n = len(literals)
	for seq in itertools.product([True, False], repeat=n):
		a = set(zip(literals, seq))

		if all([bool(disj.intersection(a)) for disj in cnf]):
			return True, a

	return False, None


# Implementacion de DPLL basada en https://davefernig.com/2018/05/07/solving-sat-in-python/
def my_dpll(Formula, assignments={}):

	numberOfLiterals = Formula[0]
	
	direcciones = Formula[1]

	print(direcciones)
	print("Direcciones")

	if len(direcciones) == 0:
		return True, assignments

	if any([len(conjuncion)==0 for conjuncion in direcciones]):
		return False, None

	variable = __select_literal(direcciones)

	new_cnf = [c for c in direcciones if (variable, True) not in c]
	new_cnf = [c.difference({(variable, False)}) for c in new_cnf]
	sat, vals = dpll(new_cnf, {**assignments, **{variable: True}})
	if sat:
		return sat, vals

	new_cnf = [c for c in direcciones if (variable, False) not in c]
	new_cnf = [c.difference({(variable, True)}) for c in new_cnf]
	sat, vals = dpll(new_cnf, {**assignments, **{variable: False}})

	if sat:
		return sat, vals
 
	return False, None


def individualTest(filename):

	testingParse = ParserDimacs("test/uf20-01.cnf")

	start_dpll = time.time()
	my_dpll(testingParse)
	end_dpll = time.time()

	print(f"TIEMPO DPLL: {(end_dpll-start_dpll)}")


	start_brute = time.time()
	bruteForce(testingParse)
	end_brute = time.time()
	print(f"TIEMPO FUERZA BRUTA: {(end_brute-start_brute)}")

def complete_Testing():

	print("")
	print("Testeando satisfacibles 20\n")


	for i in range(5):
		print(f"Test {i}, carpeta: satisfacibles20/uf20-{i:02d}.cnf")

	print("Testeando insatisfacibles 20\n")

	for i in range(15):
		print(f"Test {i}, carpeta: insatisfacibles20/uf20-0{i}.cnf")


	print("")
	print("Testeando 50\n")

	for i in range(5):
		print(f"Test {i}, carpeta: satisfacibles50/uf20-0{i}.cnf")



complete_Testing()

# exampleCNF = [{("p", False), ("q", False)}, {("p", True), ("r", False)}]
# print(example_brute_force(exampleCNF))
# print(bruteForce([3, exampleCNF]))
