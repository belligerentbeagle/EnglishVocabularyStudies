however = ["In retrospect","inhindsight","In converse","Regrettably","On the other hand","On the flip side of the coin","In reverse","Howbeit","Counter-intuitively"]
furthermore = ["To add insult to injury","To add fuel to fire","aggreviate","proliferate"]
linking = ["hitherto","intrinsically","inherently", "decidedly","indubitably","incontrovertible"]
goodphrases = ["carrot-and-stick","Gain traction","Ethos of hardwork","Enter into the fray","tinkering around the edges","austerity measures","strata of society","double edged sword","a case in point","medical realm","concerns are misplaced","frets about a future","key underlying driver","In the nick of time","existential threat",         
                "Whiling away a few hours","Give an upper hand","Tantamount to","In pursuant to","Blow the cobwebs out of one's brain","Grown accustomed to",
               "distant pipe dream", "a gale of laughter","blow hot and cold","brimming with energy","replete with sadness","untetheringthemselvesfromthe constrictions of genderroles","draw on my skills to do sth", "with investment foresight","prior to .....", "preaching the virtues of ____ ","a succession of problems","lends itself well to ____ ","could reach no conclusions as to its impact","take a hard line", "once ____ abates","for a fraction of _____", "covered by an umbrella of misconceptions","humble circumstances","concerted efforts","nothing short of ________"]
conclusion = ["To ram the point home","In a nutshell"]
latin = ["vis-a-vis","raison detre","primma donna","esprit de corps","creme de la creme","prima facie"]
quotes = ["'Education has long been viewed as the primary vehicle by which one can ascent the ladder of opportunity'","'A pessimist sees the difficulty in every opportunity; an optimist sees the opportunity in every difficulty.' --Roosevelt","'Not all readers are leaders, but all leaders are readers' -- Harry Truman ","chop down the tall poppy","Spawned a maxim of 3 necessities to win a place at a good university is 'Father's wealth, mother's information, child's stamina'"]
def prompt():
    answer = str(input("Type either 'latin','however','furthermore','quotes','good phrases','linking' or 'conclusion': "))
    reply(answer)
    return answer


def printing(target):
    length = len(target)
    length -= 1
    while True:
        if length > -1:
            print(target[length])
            length -= 1
        else:
            print(" ")
            prompt()

def reply(answer):
    print(" ")
    if answer == "however":
        printing(however)
    elif answer == "furthermore":
        printing(furthermore)
    elif answer == "conclusion":
        printing(conclusion)
    elif answer == "good phrases":
        printing(goodphrases)
    elif answer == "quotes":
        printing(quotes)
    elif answer == "latin":
        printing(latin)
    elif answer == "linking":
        printing(linking)
    else:
        prompt()
    print(" ")
    prompt()

prompt()    

    
