



while True:
    opening = open('/Users/yuxin/Desktop/words.txt','r') # open up text file
    lines = [line.rstrip('\n') for line in opening] # make a list out of the words in it
    for word in lines:
        print(word) #prints each word one by one
    useradd = input("Add any word: ") 
    if (useradd != "") and (useradd !="quit"):
        writing = open('/Users/yuxin/Desktop/words.txt','a+')
        writing.write(useradd + "\n")
        writing.close()
    elif useradd == "quit":
        opening.close()        
        exit()
    else:
        continue
    opening.close()
        

