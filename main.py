""" 
Kirjutame koos programmi, mis küsib kasutajalt, mis päev on homme (tööpäev või puhkepäev), ning väljastab vastuse põhjal sobiva sõnumi. 
Kasutaja sisestab ühe sõna: 
"tööpäev"
Või "puhkepäev" 
Kui sisestus on "tööpäev", siis kuvatakse ekraanile tekst:
Ma lähen magama, head ööd!
Kui sisestus on "puhkepäev", siis kuvatakse ekraanile tekst:
Veel üks osa Netflixist!
"""
#alusta programmi.
#Küsi kasutajalt: "mis päev on homme? (tööpäev/puhkepäev)".
#Salvesta vastus muutjuasse day.
#Kui day on võrdne sõnaga "tööpäev", siis väljasta ekraanile: "Ma lähen magama, head ööd!"
#Muidu, kui day on  võrdne sõnaga "puhkepäev", siis väljasta ekraanile: "Veel üks osa Netflixist!"
#Muidu (kui sisestus ei olnud õige), siis väljasta ekraanile: "Vale väärtus".
#Lõpeta programm.



""" day = input ("mis päev on homme? (tööpäev/puhkepäev):")

if day == "tööpäev":
    print("Ma lähen magama, head ööd!")
elif day == "puhkepäev":
    print("Veel üks osa Netflixist!")
else:
    print("Vale väärtus") """




""" # #Finantsnõustaja 
Sa tahad osta endale uue iPhone 17 Pro, aga sa oled otsustanud, et krediiti sa ei võta. Selle asemel oled sa palganud range 
# ja vastutustundliku finantsnõustaja programmi kujul.
# See programm: 
# - küsib, kui palju sul on praegu raha, 
# - võrdleb seda iPhoe 17 Pro hinnaga ( näiteks 2 500€)
# - ja annab sulle täiesti ratsionaalse, emotsioonideta soovituse. """

# print("Tere tulemast programmi 'Finantsnõustaja'!")
# print("Sinu isiklik nõustaja ei tee emotsionaalseid oste.")

# money = int(input("Kui palju raha sul on praegu?"))

# if money < 2500:
#     print("Sul pole veel piisavalt raha. Ole kannatlik ja kogu edasi!")
# elif money ==2500:
#     print("Palju õnn, saad osta uue iPhone 17 Pro sularahas!")
# else:
#     print("Saad osta iPhone 17 Pro ja veel jääb raha üle.") """

#Sammulugeja

""" Sul on eesmärk teha iga päev 10 000 sammu. Programm küsib kasutajalt, mitu sammu t on juba teinud, arvutab täitmise protsendi ja annab tagasisidet.
- Kui protsent <50: "Alles poolel teel, liigu edasi!"
- Kui protsent <75: "Tubli, oled peaaegu kohal!"
- Kui protsent >=100: "Palju õnn, oled oma eesmärgi täitnud!" """

goal = 10000
steps = int(input("Mitu sammu oled juba täna teinud?:"))

percent = (steps/goal) * 100

print(f"{percent}%")

if percent < 50:
    print("Alles poolel teel, liigu edasi!")
elif percent < 75:
    print("Tubli, oled peaaegu kohal!")
elif percent < 100:
    print("Suurepärane, oled peaaegu kohal!")
else:
    print("Palju õnn, oled oma eesmärgi täitnud!")
