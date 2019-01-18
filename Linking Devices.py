import random

phrases = {"A _ issue": ["controversial","contentious","vexed","divisive","heated","hotly debated","disputed"],
             "A _ point": ["contributory factor","determining factor","reasonable position","revealing/telling comment","provison","stipulation","on the premise that", "crux of the problem","nub of the argument"],
             "To (discuss) " : ["advance/ posit/ postulate (an argument)", "propound (a theory/ argument)","allude to"],
             "To agree _ " : ["unequivocally", "provisionally", "conditionally","unanimously","a temporary mortatorium"],
             "Oppose": ["refute","rebut","repudiate","denounce","condemn","censure (a policy)","deplore","disparage","split/divergence of opinion","culpable","excuplate","exonerate","cast aspersions on","retort","countervailing"],
             "other useful openings": ["By analogy","By comparison","This is analogous to ...", "Undeniably","undoubtedly","indisputably","arguably","of course","certainly","A case in point"],
             "Random": ["salient points/facts"],
             "A _ problem": ["It sets a precedent","It sets a dangerous precedent","imminent/impending","endemic","systematic/structural","an alarming prospect"," grave objection","bone of contention","deleterious","adverse","an impediment","stumbling block","hinderance","insuperable","insurmountable","daunting/formidable challenge","retrograte/regressive","counterproductive","irreconcilable differences","polarised positions","reprehensible","misconstrue","egregious mistake","quagmire","intransigent","intractable","to reach an impasse","to end in deadlock",],
             "A solution": ["Advocate","ameliorate","to forestall/avert/prevent","pre-empt","remedy","rectify","reconcile"," conciliate","appease","moratorium","concerted efforts","amicable solution"],
             "Criticising arguements": ["unethical","unconscionable","unprincipled","unjust","inequitable","frivolous","trivial","groundless","baseless","indefensible","untenable","uncorroborated","inconsequential","nebulous","equivocal","convoluted","fallacious","specious","exagerrated","inconclusive","procrustean measures","draconian measures","untenable","indefensible","tortuous"]
}
line = "----" * 25

while True:
    cue = input("Press enter")
    for key in phrases:
        
        print("\n" + key)
        print(line + "\n")
        for word in phrases[key]:
            print(word)

