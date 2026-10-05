""" #Alusta programmi.
#Küsi kasutajalt perekonnanime ja sugu (m või n).
#Salvesta perekonnanimi muutujasse last_name ja sugu m või n
#Kui sugu on m, siis tervita kasutajat: "Tere, härra <perekonnanimi>!"
#Kui sugu on n, siis tervita kasutajat: "Tere, proua <perekonnanimi>!"
#Muidu (kui sisestus ei olnud õige), siis tervita kasutajat: "Tere tulemast, <perekonnanimi>! (sugu ei olegi tähtis)."
#Lõpeta programm. """

last_name = input("Sisesta oma perekonnanimi:")
gender = input("Sisesta oma sugu (m või n):")
if gender == "m":
    print(f"Tere, härra {last_name}!")
elif gender == "n":
    print(f"Tere,proua {last_name}!")
else:
    print(f"Tere tulemast, {last_name}! (sugu ei olegi tähtis).")
