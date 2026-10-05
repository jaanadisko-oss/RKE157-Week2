""" #Alusta programm.
#Küsi kasutajalt joodud vee klaaside arvu.
#Salvesta väärtus muutujasse glass.
#Arvuta joodud vee kogus milliliitrites (1 klaas = 250 ml).
#Arvuta, kui suur protsent päevanormist (2000 ml) on joodud.
#Väljasta protsent ekraanile.
#Kui protsent on alla 50, siis väljasta: "Joo rohkem vett, keha vajab seda!".
#Kui protsent on 50 kuni 100, siis väljasta: "Tubli, jätka samas vaimus!".
#Kui protsent on üle 100, siis väljasta: "Suurepärane, oled oma päevase eesmärgi täitnud!".
#Lõpeta programm. """

glass = int(input("Mitu klaasi vett oled täna joonud? "))
paevanorm_ml = 2000
glass_ml = 250
drunk_ml = glass * glass_ml
percent = (drunk_ml / paevanorm_ml) * 100
print(f"Oled täitnud {percent}% päevanormist.")
if percent < 50:
    print("Joo rohkem vett, keha vajab seda!")
elif percent < 100:
    print("Tubli, jätka samas vaimus!")
else:
    print("Suurepärane, oled oma päevase eesmärgi täitnud!")
