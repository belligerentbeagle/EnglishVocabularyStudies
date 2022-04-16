


discrimination = {
	'Transgender': ["Trans text", "some policy here", "Some examples here"], 
	'Disability': ["Mental Disorders: 1, 2, 3", "Physical Incapacitation","Japan hires them to operate robots in the restaurants"]
}

technology = {
	'3D Printing': ["3D Printers has enabled low cost printing which has lowered the costs of prostethics for disabled people dramatically.","Bionics","'We are probably the first species that can influence it's own evolution'"]
}

politics = {
	'Depotism' : ["Depotism/Tyranny occurs when a nation or country is ruled by a tyrant - a ruler who governs with little regard to popular support or even the best interests of his or her people.","A political system in which an often harsh and oppressive ruler wields absolute power.","Peisistratus, First tyrant of Athens, Kim Il-Sung, Former president of N.K., established a cult of personality, Saddam Hussein, Former president of Iraq."],
	'Oligarchy' : ["An oligarchy is a ruling elite governing for its own self-interest rather than for the interest of society as a whole","An oligarchy is a political system in which a small ruling elite takes resource from everyone and gives back only to its own.","Plato, Greek philosopher who defined oligarchy as rule by the wealthy"],
	'Authoritarianism' : ["Authoritarianism is a broad category that encompasses any government where the ultimate power to make decisions for a society is vested in a specific person or a privileged class or group. They have power as they belong to a particular family (such as in aristocracies or monarchies), or militaries."]
}

# class topiccaller():
# 		def name(self):
# 			if topic == "discrimination":
# 				return "Discrimination"

while True:
	topic = input("Enter your topic (" + "discrimination" + "): ")
	print("\n__" + topic.upper() + "__")
	print("--Transgender Discrimination") # perhaps i can do regex and print a list nicely
	for elem in discrimination['Transgender']:
		# if elem == (discrimination['Transgender'])[-1]:
		# 	print(str(elem))
		# else:
		print("----" + str(elem))

