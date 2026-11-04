rezultati = []

for rinda in open("sistema.log"):
    if "ERROR" in rinda:
        rezultati.append(rinda)

print("ERROR rindu skaits:" , len(rezultati))

for rinda in rezultati[:2]:
    print(rinda)
