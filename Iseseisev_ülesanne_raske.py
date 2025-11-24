import random

# 03
# Täringud
# kuvatakse korrektne arusaadav küsimus ja hiljem vastus - 1p
# kasutaja võistleb kahe täringuga arvuti vastu - 1p
# kasutaja teeb pakkumise ning suurima täringupunktisumma võitja saab laual oleva raha endale - 2p
# kood kommenteeritud - 1p


print("====Ole valmis raha kaotama!====")  

# Mängija algne raha
raha = 100
print(f"Sul on {raha} eurot.")

try:
    # Mängija panus
    panus = int(input("Sisesta oma panus (täisarv): "))

    # Kontrollime, et panus oleks sobiv
    if panus <= 0 or panus > raha:
        print("Panus ei sobi! Panus peab olema positiivne ja mitte suurem kui sinu raha.")
    else:
        print(f"Panustasid {panus} eurot. Laual on {panus * 2} eurot.")

        # Täringute veeretamine
        mängija_summa = random.randint(1,6) + random.randint(1,6)
        arvuti_summa = random.randint(1,6) + random.randint(1,6)

        print(f"Sinu täringute summa: {mängija_summa}")
        print(f"Arvuti täringute summa: {arvuti_summa}")

        # Võitja selgitamine
        if mängija_summa > arvuti_summa:
            raha += panus  # võitja saab oma panuse tagasi + sama palju juurde
            print(f"Võitsid! Sinu raha on nüüd {raha} eurot.")
        elif mängija_summa < arvuti_summa:
            raha -= panus  # kaotasid oma panuse
            print(f"Kaotasid! Sinu raha on nüüd {raha} eurot.")
        else:
            print(f"Viik! Sinu raha jääb samaks: {raha} eurot.")
except:
    print("Viga: palun sisesta korrektne täisarv panusena.")




# 02
# Eurokalkulaator - koosta programm, mis kalkuleerib valuuta vastavalt kasutaja soovile EUR->EEK või EEK->EUR.
# kuvatakse korrektne arusaadav küsimus ja vastus
# kuvatakse veateade, kui kasutaja tegi valiku valesti
# küsitakse valuuta kogust ja tehakse arvutused
# kood kommenteeritud

print("vali kalkulaator:")  #käsklus kalkulaatori valikuks ja valiku variandid
print("a) EEK->EUR")
print("b) EUR->EEK")

valik = input("Sisesta valik (a/b): ") #käsklus valiku tegemiseks

#kurss
EEK_to_EUR = 0.063911485
EUR_to_EEK = 15.6466

try: #veakontroll
    if valik == "a":
        eek = float(input("Sisesta EEK summa: ")) #võimaldab sisestada komadega arvusid
        eur = eek * EEK_to_EUR                    #valem kursi arvutamiseks
        print(f"{eek} EEK = {eur:0.2f} EUR")      #ümardab vastuse läbi kursi valemi kahe komakoha peale
    elif valik == "b":
        eur = float(input("Sisesta EUR summa: "))
        eek = eur * EUR_to_EEK
        print(f"{eur} EUR = {eek:0.2f} EEK")
    else:
        print("Ei ole midagi sisestatud! Vali 'a' või 'b'.") #veateade, et valikut pole tehtud
except:
    print("Midagi läks nihusti! Pane numbriline väärtus.") #veateade, et sisestatud on midagi muud



# 01
# Koosta programm, mis kontrollib, kas kasutaja poolt sisestatud arv on paaris või paaritu
# kuvatakse korrektne arusaadav küsimus ja vastus - 1p
# eelnev kontroll, kas kasutaja ei lisanud arvu või pani nulli - 1p
# kood mis teavitab paaris või paaritust arvust - 1p
# kuvatakse programmi pealkiri - 1p
# kood kommenteeritud - 1p

print("=====ARVU KONTROLL!=====")       #programmi pealkiri

try:                                    #eelkontroll, et sisestus oleks õige
    arv = int(input("Kontrolli arvu:")) #küsimus arvu kontrolliks, mis seotud valemiga
    if arv == 0:                        #välistab kontrollis nulli kasutuse
        print("miskit läks nihu!")
    else:
        valem = arv % 2                 #jäägiga jagamine 2-ga, et selgitada, kas sisetatud arv on paaris või paaritu
        if valem == 0:                  #näitab, et jagamisel jääki pole
            print("see on paarisarv")
        else:
            print("see on paaritu arv")
       
except:
    print("Miskit läks nihu!")          #kontrolli vastus




    #prooviks täna ja homme