from cs50 import get_string


def main():
    cardnumber = GetCardnumber("Card number: ")
    digits = NumberOfDigits(cardnumber)
    VerifyCardLenghts(digits)
    LuhnAlgoritm(cardnumber, digits)
    VerifyBrand(cardnumber, digits)

#get cardnumber
def GetCardnumber(promt):
    while True:
        cardnumber = get_string(promt)
        card = int(cardnumber)
        if card > 0:
            break
    return cardnumber

#number of digits
def NumberOfDigits(cardnumber):
    digits = len(cardnumber)
    return digits

#check card lenghts
def VerifyCardLenghts(digits):
    if digits < 13 or digits > 17 or digits == 14:
        print("INVALID")
        exit(0)

#Luhn Algotitmes
def LuhnAlgoritm(cardnumber, digits):
    sum = 0
    x = 1
    for i in cardnumber:
        number = int(i)
        if digits == 14 or digits == 16:
            if x % 2 == 1:
                number *=2
                if number > 9:
                    number -=9
            sum += number
            x += 1
        if digits == 13 or digits == 15:
            if x % 2 == 0:
                number *=2
                if number > 9:
                    number -=9
            sum += number
            x += 1
    if not (sum % 10) == 0:
        print("INVALID")
        exit(0)

#get first 2 figures, verify brand
def VerifyBrand(cardnumber, digits):
    first = int(cardnumber[0]) * 10
    second = int(cardnumber[1])
    two = first + second
    if two == 51 or two == 52 or two == 53 or two == 54 or two == 55 and digits == 16:
        print("MASTERCARD")
    elif int(two / 10) == 4 and (not digits == 15):
        print("VISA")
    elif two == 34 or two == 37 and digits == 15:
        print("AMEX")
    else: print("INVALID")


if __name__ == "__main__":
    main()


