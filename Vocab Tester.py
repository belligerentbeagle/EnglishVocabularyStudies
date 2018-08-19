import random

def checkforword():
    checkWord = False	  #Change to true if checking word
    if checkWord == True: #checking words
        if "exonerate" in name:
             print(True)
        else:
            print(False)
            
    

name = ["hotchpotch", "quaint", "unremittingly", "lineage", "mushroomed",
            "austere", "facade", "harness", "hustle and bustle", "illustrious", "feat", "painstaking", "laudable vs culpable", "empirical","cognitive","indigenous","cardinal","oblong","spatial","causality","notion","encode","profound","disposition","placid","transgressor","restitute","eschew","excavate","since time immemorial","rudimentary","uncharted territories","kitty","well-heeled","maiden","audacious","reside","vicinity","artisanal","snotty","relegate","seditious","stigma","prevalent","tunnel vision","camadarie","ecstacy","cement","emulate","stellar achievement","underpin","nexus","culpable vs laudable","precipitate","full-fledged","unequivocal vs ambiguous","novel","ambiguous","stifle","inicimal","fervently","groteque","adage","dire","dysfunctional","transmorgrify","channel","go-getter","horde","covenant","scuffle","dole out","obsolescence","strenuous","eulogy","ludicrous","demise","rank and file","prevail","epitomise","knack","aplomb","unscathed","precept","self-effacing","relish","winsome","metamorphosis","peevish","sinuous","mantle","callous","preponderance"
            "ramification","glisten","cryptic","nihilistic","chasm","finesse",
            "resolute","fervour","teeming with","totem","emanate","point-blank"
            ,"unnerving","inaugural","sandblasted","careen","emblematic","anachronistic", "antiquated", "inconsequential","apt","omniprescence vs ubiquitous",
            "promulgate","steel","emaciate","condemn","forsaken","deftly","adroit","adept","miasma","stump","stump","diminutive","tantamount to","delirious","ominous","derelict","circumstantial",
            "lauel (to rest on one's laurel","suffuse","recursive"
            ,"implicitly","proponents","indelible","foraging","tranquil","rustic","idyllic","sanctuary","undulating","meander","congregate","pristine","exodus","permeate","straddle","kaleidoscope","bequeathe","luxuriant","sentinel",
            "estuarine","galvanise","wafted through","diplomacy","asymmetric","anemone","amenable","efficacy","aftermath","detestable","abominable","overarching","collude","adverse","probable","exacting","egregious","pragmatic","onerous","boisterous","prejudice"
        ,"susceptible","regurgitate","probity","parity","idiocy","idiosyncrasy","eccentric",
            "prima donna","impede","unemcumbered","pelt","gruelling","esprit de corps","echelon","fraught with","meager","arbitrary","repatriate","astronomical","exorbitant","transient","assuage","proffer","vis-a-vis","purview","protracted","inequitable vs parity","in pursuant to", "imperative","tendril","awning","miniscule vs diminutive","emanate","hapless","rogue",
        "rendevouz","serenity vs tranquility","conflagration","flail","cognizant","mounting","indulge","subsume","shoestring budget","belligerent","toll","outpace","stark",
            "oncologist","geriatric care","cartel","postulate","allude to","deplore","disparage","exonerate","to cast aspersions","countervailing","retort","predominant","intravenously","entail","decimate","laurel","regress","lull","aforementioned","frivolous","stringent","exemplary","avid","rehabilitate","latter","endeavour","shrewed","crafty","bestial","treacherous","implicate","banister","instinctively","foiled",
        "porous","potent","surreptitious vs clandestine vs collude","underscore","clandestine","unanimously","disconcerting","shrill","brute","contraption","tenets","shackles","sanguine","alleviate","insurmountable","amalgamation",
        "pundit","intriguing","delactable","lingua franca","inadvertently","exuberant","antics","erroneous","bricks and mortar","advent","trajectory","mundane","automaton","endorse","indiscriminately","creme de la creme","ubiquitous","equity",
            "perpetrate"]
setA = ["tributaries","statuesque","rev","relentless","commodity","intrepid","remnant","burgeon","keep sth at bay","stave off","persona non grata","pedigree","unilaterally","menace","exacerbate","petrified","prowess","gaberdine","cordovan","swaggered","impertinent",
        "incapcitated","beak","euthanasia","rapine","awash","wiry","impotent","anaemic","elicit","taut"
            ,"wispy","ringlets","wade","prim","stricture","trapezoid","gaunt","cirrus","cumulus","meringues","sleek",
            "distended","prominent","champing","intricate","variegated","devoid","outlandish",
            "belching","deep pockets","haggle over","solitude","intertwine","compelled","contemptible","malice","contemn","veritable","pilgrimage","roughshod","contemporary","eloquence",
            "archaic"]
setB = ["coddled and cossetted","mogul","reprieve","alluring","incessant","grow accustom to","distant pipe dream","salient","appropriation","whiling away the time","add insult to injury","ram the point home","correlation","counter-intuitively","predispose","inclination","doting","disparate","girth"]
setC = ["fortified","homespun","incongruous","enervate","sidle","inscription","menace","traverse","belligerent","garret","studious",
        "endow","technocrat","conspicuous","incur the wrath of","lolly",
        "punting","in lieu of","largesse","plutocracy","coerce",
        "chivalrous","bawl out","deluge","succumb","deft","proffer","construe","exhort","iniquities"] #15 Jan (Sun)
setD = ["compel","prevalent","opine","toil","guzzles","voluminous"] #21 Jan (Sat)
setE = ["versatile","tout","panacea","upending","palpable","guise","existential","academia",
        "entity","fret","paranoia","advocate","cite","potemkin","pedagogy","nonplussed"]#5 Feb(Sun)
setF = ["permeate","fallacy","per se","exemplify","analogous to","bestowed","plethora","realm","blinkered view","supersede","egalitarian","elitist","in tandem","resonance","impoverish"
        ,"tenor","stasis","unwitting","perpetuate","expedite","noble","engender","remedial","entrenched","conjure","archetypal","quintessential","circumspect","omnipresent","outset","feral","guffaw","slither","stasis","indelible",
        "riven","flatline","incessant"]#12 Feb(Sun)
setG = ["punitive","ascribed","stratospheric","pivotal","untennable","inexorably","seminal","multitudinous","irrespective"] #19 Feb (Sun)
setH = ["impartial","austerity measures","pious","tinkering around the edges","draconian","demurrals","luminary","into the fray","impotent","hubristic","punitive","ascribed","attrition","ethos","accolades","stratify","gain traction","in retrospect","proliferate","instill","consesnsus","confer","perch","gingerly","hitch","scourge","carrot-and-stick"] #26 Mar 2017
setI = ["rejoinder: clever witty reply", "riposte: quick, witty response", "countervail: to use equal force again","reciprocate: to give/act in turn following the lead of another",
        "refute: to produce evidence or proof that an arg is wrong", "retort: to reply in a sharp, retaliatory way","inquisitive: Having the nature of an investigator","frenetic: frantic and frenzied",
        "angst: a feeling of anxiety, dread or anguish","irascible: easily irritated/annoyed; prone to losing temper","niggling: petty,annnoying","officious: asserting authority in an overbearing manner",
        "vexation: frustration/annoyance resulting from some action/statement"]
setJ = ["social affirmation","conformity","trodden","pervasive","amorphous","truncated","condoning","credence","leveraging","herd","vying","synonymous","batter","stoic","trivial","composed by/of","minute"
        ,"nebulous","reel in","cusp","utilitarian","proclivities","permutations","glean","trance","blear","debauchery","douse",
        "primeval","jarr","assuage","unencumbered","rites","plein","call at","call away","call by","call down upon","call in"]
setK = ["dexterity", "sprawling", "reckon", "indisputable", "enthrall", "meticulous","immaculate", "fastidious","discharge","forays","due diligence","touted","parochial","vouch","sentiment","rife","concur","posit","ensconcing","masquerade","presenteeism","scaffold"]
setL = ["sacrosanct", "foppish", "cathartic", "milieu", "genial", "in the throes", "sheepish", "gale", "acclimatised to", "inkling", "yesteryear", "intrinsically", "indomitable", "at the forefront"]
setM = ["revamp","drudgery","succession","overhaul","bolting","vernacular","periodically","forthcoming","inpart", "pro bono","demography","yogic","accrue","caricature","anarchic","adulterate","arboreal","plod ahead/through/on","abate","impediment","steel","bard","run of the mill","be in a rut","pilot-programmes","siphon off","afoot","oligarch","proverbially","replete with","folly","zealot","pandered","rabble-rousing",
        "populous","presided over","dud","illict","glitzy","perversely","quagmire","propitious","upperhouse","sap","chauvinist","hamstring"]
setN = ["preaching the virtues of","edgeways","bedivilling","inroads","decry","intricate","ordain","prudent","zoonotic","pertain","avian","gain a foothold","drawn on","veracity","envisage","blundering","concerted","morbidity","profanity","brain drain","prudish","emancipation","constrictions","ensue","onerous"]
setO = ["fall away", "incalculable","social mores","vex","gateway to/ for something","kiki, do you love me", "en masse","bureaucrats","wallah","ploy","exodus","construe","moped","bigot","wahhabism","apprehension","perilous","contempt","callous","unorthodox","persona-non-grata"]
setP = ["anachronistic","squalid","dinghy","wanton","virulently","fervour","precarious","parable","reproachfully","precocious","sultry","aficionado","faddish","trawling","arcana","unnerve","bestride","neophyte","caveat","erudite","curator","corroborate","sacrosanct","monoliths","precarious","fervour","ascetic","inoculation","resignedly","morbidity rate"] #19th August

hard = [" "]
name.extend(hard)
name.extend(setB)
name.extend(setA)
name.extend(setC)
name.extend(setD)
name.extend(setE)
name.extend(setF)
name.extend(setG)
name.extend(setH)
name.extend(setI)
name.extend(setJ)
name.extend(setK)
name.extend(setL)
name.extend(setM)
name.extend(setN)
name.extend(setO)
name.extend(setP)

def printsets(target): #Used in printsetsornot function, to simplify when adding a new set
    print(" ")
    which = 0
    while True:
        if which<len(target):
            print(target[which])
            which += 1
        else:
            print(" ")
            break

def printsetsornot(target):
        if target == ("setA"): #Change here each time you add a new set
            printsets(setA)
        elif target == ("setB"):
            printsets(setB)
        elif target == ("setC"):
            printsets(setC)
        elif target == ("hard"):
            printsets(hard)
        elif target == ("setD"):
            printsets(setD)
        elif target == ("setE"):
            printsets(setE)
        elif target == ("setF"):
            printsets(setF)
        elif target == ("setG"):
            printsets(setG)
        elif target == ("setH"):
            printsets(setH)
        elif target == ("setI"):
            printsets(setI)
        elif target == ("setJ"):
            printsets(setJ)
        elif target == ("setK"):
            printsets(setK)
        elif target == ("setL"):
            printsets(setL)
        elif target == ("setM"):
            printsets(setM)
        elif target == ("setN"):
            printsets(setN)
        elif target == ("setO"):
            printsets(setO)
        elif target == ("setP"):
            printsets(setP)
        else:
            vocab()
        activate()
 

def wordcount():
    print(str(len(name))+ " words in bank") #declare no. of words
    global data
    data = input("Enter number of vocab:") #prompts user and stores in "data"
    return data

def vocab():
    print(" ")          #leaves spacing
    words = 0
    number = int(data)
    
    while True:
        if number > 0:
            tom = random.choice(name)
            print(tom)
            number -= 1
            words += 1
        else:
            print(" ")
            points = input("Points:")
            points = str(points)
            word = str(words)
            print(points+"/"+word)
            if points == word:
                print("Wonderful!!")
            if float(points)/float(word) > 0.80 and float(points)/float(word)<1.0:
                print("not bad!")
            enterhardwords()
            break


def enterhardwords():
    print(" ")
    toughwords = input(str("Hard words(enter space when complete): "))
    if toughwords != " ":
        hard.append(toughwords)
        enterhardwords()
    else:
        print(" ")
    
    
def activate():
    while True:
            wordcount()
            printsetsornot(data)
            vocab()
#activate() # Comment this if you want automatic 

def automaticpopup():
    noofwords = random.choice((1,2,3,4,5,6,7,8,9,10))
    while True:
        if noofwords > 0:
            foreignword = random.choice(name)
            print(foreignword)
            noofwords -= 1
        else:
            break
    response = input("Press space, then enter to continue OR type 'manual' for Manual mode: ")
    if response == " ":
        automaticpopup()
    elif response == "manual":
        activate()

automaticpopup()
