counties = ["Arapahoe","Denver","Jefferson"]
if counties [1] == "Denver":
    print (counties[1])
if "El Paso" in counties:
    print("El Paso is in the list of counties")
else:
    print("El Paso is not in the list of counties")
if "Arapahoe" in counties and "El Paso" not in counties:
    print("Only Arapahoe is in the list of counties")
else:
    print("Arapahoe is in the list of counties and El Paso is not in the list of counties")
for county in counties:
    print(county)
    