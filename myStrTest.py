name= "NamrataG"
if name.endswith("G"):
    addName= name[:-1] + " Guragain"
    print (addName)
else:
    print (name+ "Acharya")


name= ["NamrataG", "SampadaA", "SagunA", "SharadA"]
if name[0].endswith('G'):
    name1= name[0][:-1]+ " Guragain"
    name.append(name1)
    print(name)
else:
    print(name)


