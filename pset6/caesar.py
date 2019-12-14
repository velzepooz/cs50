from sys import argv
from cs50 import get_string

def main():
    plaintext, key = GetPlaintext(argv)

    cipher = Caesar(plaintext, key)
    print("ciphertext: " + cipher)
    #print()




#check argv, getting plaintext
def GetPlaintext(argv):
    if len(argv) == 2:
        if int(argv[1]) > 0:
            key = int(argv[1])
            plaintext = get_string("plaintext: ")
            return plaintext, key
        else:
            print("Usage: ./caesar key")
            exit(1)
    else:
        print("Usage: ./caesar key")
        exit(1)

#Shift
def Shift(c):
    r = c
    if c >= 65 and c <= 90: r -=65
    elif c >= 97 and c <= 122: r -= 97
    return r

#Caesar
def Caesar(plaintext, key):
    cipher_i = []
    cipher = cipher_i
    while True:
        for i in plaintext:
            if i >= 'A' and i <= 'Z':
                    cipher_i = (Shift(ord(i)) + key) % 26 + 65
                    cipher = chr(cipher_i)
            elif i >= 'a' and i <= 'z':
                    cipher_i = (Shift(ord(i)) + key) % 26 + 97
                    cipher = chr(cipher_i)
            else:
                cipher_i = ord(i)
                cipher = chr(cipher_i)
        if len(plaintext) == 0:
            break
    return(cipher)

if __name__ == "__main__":
    main()

