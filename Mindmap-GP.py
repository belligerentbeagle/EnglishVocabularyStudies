


discrimination = {
					'Transgender': ["Trans text", "some policy here", "Some examples here"], 
					'Disability': ["Mental Disorders: 1, 2, 3", "Physical Incapacitation","Japan hires them to operate robots in the restaurants"]
					}

technology = {
	'3D Printing': ["3D Printers has enabled low cost printing which has lowered the costs of prostethics for disabled people dramatically.","Bionics","'We are probably the first species that can influence it's own evolution'"]
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

