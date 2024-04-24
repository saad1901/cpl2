radix_mapping = {
    'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12,
    'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24,
    'Z': 25, 'a': 26, 'b': 27, 'c': 28, 'd': 29, 'e': 30, 'f': 31, 'g': 32, 'h': 33, 'i': 34, 'j': 35, 'k': 36,
    'l': 37, 'm': 38, 'n': 39, 'o': 40, 'p': 41, 'q': 42, 'r': 43, 's': 44, 't': 45, 'u': 46, 'v': 47, 'w': 48,
    'x': 49, 'y': 50, 'z': 51, '0': 52, '1': 53, '2': 54, '3': 55, '4': 56, '5': 57, '6': 58, '7': 59, '8': 60,
    '9': 61, '+': 62, '/': 63
}

hexadecimal = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'a': 10, 'b': 11, 'c': 12,
    'd': 13, 'e': 14, 'f': 15
}

def getKey(dictionary, value):
    for key, val in dictionary.items():
        if val == value:
            return key
    return None

def Decoding(input):
    bstring = ""
    for i in range(0, len(input), 6):
        a = input[i:i+6]
        b = 0
        for j in a:
            b = b * 2 + int(j)
        value = getKey(radix_mapping, b)
        if value is not None:
            t = format(ord(value), '08b')
            bstring += t
    return bstring

def Encoding(input):
    for i in range(0, len(input), 6):
        a = input[i:i+6]
        b = 0
        for j in a:
            b = b * 2 + int(j)
        value = getKey(radix_mapping, b)
        if value is not None:
            print(value, end='')

def conversion(x):
    result = ""
    for i in range(0, len(x), 4):
        a = x[i:i+4]
        b = 0
        for j in a:
            b = b * 2 + int(j)
        value = getKey(hexadecimal, b)
        if value is not None:
            result += value
    return result

x = input("Enter a binary number\n")
print("Hexadecimal value is: ")
print(conversion(x))
print("\nRadix value is: ")
Encoding(x)
print("\nDecoded binary value is:")
r = Decoding(x)
print(r)
print("\nConverted back to hexadecimal value is:")
print(conversion(r))
