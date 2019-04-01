

année = int(input("entrer une année a tester"))
bissextile = False

if année % 400 == 0 :
	bissextile =True
elif année % 100 == 0:
    bissextile = True
elif année % 4 == 0:
    bissextile = True
else:
    bissextile = False

if bissextile :
    print("l'année {} est une année bissextile".format(année))
else:
    print("l'année {} n'est pas une année bissextile".format(année))

