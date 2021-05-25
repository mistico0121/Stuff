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


exampleCNF = [{("p", False), ("q", False)}, {("p", True), ("r", False)}]

testingParse = ParserDimacs("uf20-01.cnf")
print(testingParse)

print("DPLL: ")
print(dpll(testingParse[1]))

print("Fuerza Bruta: ")

print(bruteForce(testingParse))

# print(example_brute_force(exampleCNF))
# print(bruteForce([3, exampleCNF]))
