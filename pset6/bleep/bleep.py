from cs50 import get_string
from sys import argv


def main():

    Bann(argv)
    words = Openning(argv)
    message, messagelist = Promt()
    Check(messagelist, words, message)

#check banned-list file typed
def Bann(argv):
    if not len(argv) == 2:
        print("Usage: python bleep.py dictionary")
        exit(1)

#open banned-list file, initialising words in list
def Openning(argv):
    words = set()
    list = open(argv[1], "r")
    for line in list:
        words.add(line.rstrip("\n"))
    list.close()
    return words

#promt message to censor, make message text to lowercase
def Promt():
    message = get_string('What message would you like to censor?\n')
    messagelist = (message.lower()).split()
    return message, messagelist

#check message on censored words, hash and print it back
def Check(messagelist, words, message):
    message = message.split()
    var = 0
    for i in messagelist:
            if i in words:
                message[var] = '*' * len(i)
            var += 1
    print(' '.join(message))

if __name__ == "__main__":
    main()
