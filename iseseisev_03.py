import turtle
import random

#Iseseisev töö nr 3

# Kilpkonn
# Kirjutada programm, mis lubab kasutajal valida kujundite tüübi (viisnurk, ring, ruut või suvaline) ja arvu. Programm joonistab seejärel antud arvu kujundeid valitud tüübiga või juhul, kui valik on “suvaline”, valib programm ise juhuslikult kujundi tüübi iga kujundi jaoks.

# Kõik kujundite joonistamise käsud peavad olema kirjutatud eraldi funktsioonidesse. Näiteks funktsioon joonista_ruut() või joonista_viisnurk(). Pärast joonistamist peab programm pakkuma võimalust sisestada uued väärtused või väljuda programmist, jättes sisendi tühjaks.

# Näiteks:
# Millist kujundit soovid joonistada (viisnurk, ring, ruut, suvaline)? Suvaline
# Mitu kujundit soovid joonistada? 5
# [Joonistab 5 kujundit, igaüks juhuslikult valitud tüübiga suvalistesse kohtadesse]
# Soovid jätkata?


#erinevad kujundid "def" funktsiooniga välja kirjutatud - "def" ja "random.choice" funktsiooni aitas välja selgitada AI
def joonista_ruut():
    for _ in range(4):
        turtle.fd(100)
        turtle.lt(90)

def joonista_ring():
    turtle.circle(50)

def joonista_viisnurk():
    for _ in range(5):
        turtle.forward(75)
        turtle.left(72)

def joonista_suvaline():                                            
    kujundid = [joonista_ruut, joonista_ring, joonista_viisnurk]
    random.choice(kujundid)()


# programm, mille pani paika AI..."break" ja "while true" funktsiooni oleks otsind kauakaua
while True:
    valik = input("Millist kujundit soovid joonistada (viisnurk, ring, ruut, suvaline)? ")
    if valik == "":
        print("Programm lõpetatud.")
        break

    arv = int(input("Mitu kujundit soovid joonistada? "))

    for _ in range(arv):
        turtle.penup()
        turtle.goto(random.randint(-200, 200), random.randint(-200, 200))
        turtle.pendown()

        if valik == "ruut":
            joonista_ruut()
        elif valik == "ring":
            joonista_ring()
        elif valik == "viisnurk":
            joonista_viisnurk()
        elif valik == "suvaline":
            joonista_suvaline()
        else:
            print("Tundmatu valik!")
    
    #lõpetamise jupi panin ise 
    lopetamine = input("Kas soovid jätkata?") 
    if lopetamine == "jah":
        print(valik)
    elif lopetamine =="ei":
        print("Head aega!")
        break
    else:
        print("Tundmatu valik, head aega!")
        break


turtle.done()