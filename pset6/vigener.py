from sys import argv
from cs50 import get_string

def main():
    plaintext, key = GetPlaintext(argv)
    print("ciphertext: ", end = "")
    Viginer(plaintext, key)
    print()




#check argv, getting plaintext
def GetPlaintext(argv):
    if len(argv) == 2:
       # key = int(argv[1]
        if not str.isalpha(argv[1]):
            print("Usage: ./caesar key")
            exit(1)
        else:
            plaintext = get_string("plaintext: ")
            key = argv[1]
        return plaintext, key
    else:
        print("Usage: ./caesar key")
        exit(1)

#Shift
def Shift(c):
    r = c
    if c >= 65 and c <= 90: r -=65
    elif c >= 97 and c <= 122: r -= 97
    return r

#Vigener
def Viginer(plaintext, key):
    cipher_i = []
    cipher = cipher_i
    var = 0
    for i in plaintext:
        if i >= 'A' and i <= 'Z':
            cipher_i = (Shift(ord(i)) + Shift(ord(key[var]))) % 26 + 65
            cipher = chr(cipher_i)
            var += 1
            if var > len(key) - 1: var -= var
        elif i >= 'a' and i <= 'z':
            cipher_i = (Shift(ord(i)) + Shift(ord(key[var]))) % 26 + 97
            cipher = chr(cipher_i)
            var += 1
            if var > len(key) - 1: var -= var
        else:
            cipher_i = ord(i)
            cipher = chr(cipher_i)
        print(cipher, end = "")

if __name__ == "__main__":
    main()

