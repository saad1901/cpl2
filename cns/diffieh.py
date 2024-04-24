def prime_checker(p):
    if p < 2:
        return -1
    elif p > 2:
        for i in range(2, int(p**0.5) + 1):
            if p % i == 0:
                return -1
    return 1

def primitive_check(g, p, L):
    for i in range(1, p):
        L.append(pow(g, i) % p)
    for i in range(1, p):
        if L.count(i) != 1:
            L.clear()
            return -1
    return 1

while True:
    P = int(input("Enter P: "))
    if prime_checker(P) == -1:
        print("Number is not prime, Please enter again!")
    else:
        break

l = []
while True:
    G = int(input(f"Enter the primitive root of {P}: "))
    if primitive_check(G, P, l) == -1:
        print(f"Number is not a primitive root of {P}, please try again!")
    else:
        break

while True:
    Alice = int(input("Enter the private key of Alice: "))
    Bob = int(input("Enter the private key of Bob: "))
    Eve = int(input("Enter private key of Eve: "))
    if Alice >= P or Bob >= P or Eve >= P:
        print(f"Private key of all users should be less than {P}!")
    else:
        break


y1, y2, y3 = pow(G, Alice) % P, pow(G, Bob) % P, pow(G, Eve) % P


aliceGenerated, bobGenerated = pow(y2, Alice) % P, pow(y1, Bob) % P
eveGeneratedfromAlice, eveGeneratedfromBob = pow(y1, Eve) % P, pow(y2, Eve) % P

print("Alice's Generated Key:", aliceGenerated)
print("Bob's Generated Key:", bobGenerated)
print("Eve's Generated Key from Alice:", eveGeneratedfromAlice)
print("Eve's Generated Key from Bob:", eveGeneratedfromBob)

if aliceGenerated == eveGeneratedfromAlice and bobGenerated == eveGeneratedfromBob:
    print("Keys have been exchanged successfully")
else:
    print("Keys have not been exchanged successfully")
