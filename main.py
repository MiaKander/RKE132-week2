""" 
Kirjutame koos programmi, mis küsib kasutajalt, mis päev on homme (tööpäev või puhkepäev), ning väljastab vastuse põhjal sobiva sõnumi.
Kasutaja sisestab ühe sõna:
"tööpäev" või "puhkepäev" 
Kui sisestus on "tööpäev", siis kuvatakse ekraanile tekst:
Ma lähen magama, head ööd!
Kui sisestus on "puhkepäev", siis kuvatakse ekraanile tekst:
Veel üks osa Netflixist
"""

#alusta programmi
#küsime kasutajalt, mis päev on homme? (tööpäev/puhkepäev)
#salvesta vastus muutujasse day
#kui day on võrdne sõnaga "tööpäev", siis kuva ekraanile tekst "Ma lähen magama, head ööd!"
#kui day on võrdne sõnaga "puhkepäev", siis kuva ekraanile tekst "Veel üks osa Netflixist"
#muidu (kui sisestus ei olnud õige), siis väljasta ekraanile "vale väärtus".
#lõpeta programm 

""" day =input("mis päev on homme? (tööpäev/puhkepäev):")
if day == "tööpäev":
    print("ma lähen magama, head ööd!")
elif day == "puhkepäev":
    print("veel üks osa Netflixist")
else:
    print("vale väärtus") """


#finantsnõustaja
""" Sa tahad osta enale uue iPhone 17 Pro, aga oled otsustanud, et krediiti ei saa võtta. Selle asemel oled sa palkanud endale range ja vastutustundliku finantsnõustaja programmi kujul.
See programm:
küsib, kui palju sul on praegu raha
võrdleb seda iPhone 17 Pro hinnaga (näiteks 2500 €), ja annab sulle täiesti ratsionaalse, emotsioonideta soovituse. """

""" print("Tere! Ma olen sinu finantsnõustaja.")
print("Sinu isiklik nõustaja ei tee emotsionaalseid oste.")
#int ette kui peab sisestama numbreid, mitte sõnu
money = int(input("Kui palju sul on praegu raha? "))

if money < 2500:
    print("Sa ei saa veel endale iPhone osta. Ole kannatlik ja kogu edasi!")
elif money == 2500:
    print("Palju õnne, saad osta endale uue iphone 17 Pro!")
else:
    print("Sa saad osta endale iphone 17 Pro ja jääb veelgi raha üle!)") """

#sammulugeja

""" Sul on eesmärk teha iga päev 10 000 sammu. Programm küsib kasutajalt, mitu sammu ta on juba teinud, arvutab täitmise protsendi ja annab tagasisidet.
Kui protsent <50: "Alles poolel teel, liigu edasi!"
Kui protsent < 75: "Tubli, oled peaaegu kohal!"
Kui protsent >= 100: "Palju õnne, oled oma eesmärgi täitnud!" """

goal = 10000
steps = int(input("Mitu sammu oled sa juba teinud?"))

percent = (steps / goal) * 100

if percent < 50:
    print("Alles poolel teel, liigu edasi!")
elif percent < 75:
    print("Tubli, oled peaaegu kohal!") 
elif percent < 100:
    print("Suurepärane, oled peaaegu kohal!")
else:
    print("Palju õnne, oled oma eesmärgi täitnud!")