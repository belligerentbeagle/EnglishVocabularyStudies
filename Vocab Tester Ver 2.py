import os, random, math

#initialisation
directoryoffile = '2500words.txt'
wordfile = open(directoryoffile, "r")
wordlist = []
for word in wordfile:
    length = len(word)
    word = (word.strip('\n')).strip(" ")
    word = [''.join(word[0:length])]
    wordlist += word
#print(wordlist)

print(str(len(wordlist)) +" words")
print("-"*40)
#Tester
while True:
    for i in range(0,4):
            print(random.choice(wordlist))
    print("-"*40)
    choice = input("'Manual' or Enter for auto: ")
    print("-"*40)
    if choice == "manual":
        number = int(input("Number of words wanted: "))
        print("-"*40)
        for i in range(0,number):
            print(random.choice(wordlist))
        print("-"*40)
    elif choice == "":
        for i in range(0,4):
            print(random.choice(wordlist))
        print("-"*40)
    
        


