def prime_checker(p):
	# Checks If the number entered is a Prime Number or not
	if p < 1:
		return -1
	elif p > 1:
		if p == 2:
			return 1
		for i in range(2, p):
			if p % i == 0:
				return -1
			return 1


def primitive_check(g, p, L):
	# Checks If The Entered Number Is A Primitive Root Or Not
	for i in range(1, p):
		L.append(pow(g, i) % p)
	for i in range(1, p):
		if L.count(i) > 1:
			L.clear()
			return -1
		return 1


l = []
while 1:
	P = int(input("Enter P : "))
	if prime_checker(P) == -1:
		print("Number Is Not Prime, Please Enter Again!")
		continue
	break

while 1:
	G = int(input(f"Enter The Primitive Root Of {P} : "))
	if primitive_check(G, P, l) == -1:
		print(f"Number Is Not A Primitive Root Of {P}, Please Try Again!")
		continue
	break

# Private Keys

while 1:
	Alice , Bob,Eve = int(input("Enter The Private Key Of Alice  : ")), int(
	input("Enter The Private Key Of Bob : ")),int(input("Enter The Private Key Of Eve : "))
	if Alice >= P or Bob >= P or Eve>=P:
		print(f"Private Key Of Both The Users Should Be Less Than {P}!")
		continue
	break

# Calculate Public Keys
y1, y2 ,y3= pow(G, Alice) % P, pow(G, Bob) % P ,pow(G, Eve) % P 

# Generate Secret Keys
aliceGenerated, bobGenerated ,eveGeneratedfromAlice,eveGeneratedfromBob = pow(y3, Alice) % P, pow(y3, Bob) % P ,pow(y1,Eve)% P,pow(y2,Eve)%P

print(aliceGenerated, bobGenerated ,eveGeneratedfromAlice,eveGeneratedfromBob)

if aliceGenerated == eveGeneratedfromAlice and bobGenerated==eveGeneratedfromBob:
 	print("Keys Have Been Exchanged Successfully")
else:
	print("Keys Have Not Been Exchanged Successfully")
