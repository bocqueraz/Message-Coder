import string
import random
import time
import os


def waiting(x):
    y = 0
    while (y < x):
        os.system("cls")
        print("Loading Document")
        time.sleep(0.5)
        os.system("cls")
        print("Loading Document.")
        time.sleep(0.5)
        os.system("cls")
        print("Loading Document..")
        time.sleep(0.5)
        os.system("cls")
        print("Loading Document...")
        time.sleep(0.5)
        os.system("cls")
        y = y+1

os.system("cls")
print("--------------------------------------------------------------------------")
print("Choose between coding and decoding a message!\nFor the first option write coding, for the second write decoding.")
choice = input()

if choice == "coding" or choice == "Coding":

    alphabeta = list(string.ascii_lowercase)
    codedalphabet = list(string.ascii_lowercase)
    alphabetA = list(string.ascii_uppercase)
    number = list(string.digits)
    punctuation = list(string.punctuation)
    seednumber = random.randrange(100000)
    times = -1
    x = 0

    waiting(5)

    OriginalMessage = input("Give your message please!\n")
    SeparatedMessage = list(OriginalMessage)
    random.seed(seednumber)
    random.shuffle(codedalphabet)
    x = len(alphabeta)
    for x in range(1, x+1):
        times = times+1
        letterv2 = alphabeta[times]
        globals()['letter%s' % letterv2] = codedalphabet[times]

    x = 0

    for count, value in enumerate(SeparatedMessage):
        if value == " ":
            x = x+1
        else:
            SeparatedMessage[count] = globals()['letter%s' % value]

    print("------------------------------------")
    print("Your codded message is", "".join(SeparatedMessage))
    print("Your seed ID is", seednumber)
    print("------------------------------------")

elif choice == "decoding" or choice == "Decoding":

    alphabeta = list(string.ascii_lowercase)
    codedalphabet = list(string.ascii_lowercase)
    times = -1
    x = 0

    waiting(5)

    Codedmessage = input("Give your codded message!\n")
    seednumber = input("Give the seed!\n")
    SeparatedcodedMessage = list(Codedmessage)
    random.seed(int(seednumber))
    random.shuffle(codedalphabet)
    x = len(alphabeta)
    for x in range(1, x+1):
        times = times+1
        letterv2 = codedalphabet[times]
        globals()['letter%s' % letterv2] = alphabeta[times]

    x = 0

    for count, value in enumerate(SeparatedcodedMessage):
        if value == " ":
            x = x+1
        else:
            SeparatedcodedMessage[count] = globals()['letter%s' % value]

    print("------------------------------------")
    print("The original message is", "".join(SeparatedcodedMessage))
    print("------------------------------------")

else:
    print("Please choose!")
