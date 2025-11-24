import turtle

# Harjutus 03.1
# Loo muutuja nimi, mis sisaldab kasutaja nime (string)
# Loo muutuja vanus, mis sisaldab kasutaja vanust (integer)
# Loo muutuja keskmine_hinne, mis sisaldab kasutaja keskmist hinnet (float)
# Trüki välja lause, mis ühendab kõik kolm muutujat, nt: “Karin , 18 aastat vana ja keskmine hinne on 4.7”
# Kasuta väljatrükkimisel ainult komasid (,)

nimi = "Juhan"
vanus = 58
pikkus = 1.80


print(nimi,",", vanus,"aastat vana ja pikkus on", pikkus, "m")
print(nimi+", "+str(vanus)+" aastat vana ja pikkus on "+str(pikkus)+"m")


# Harjutus 03.3
# Loo muutuja sihtkoht, mis sisaldab reisi sihtkohta (string)
# Loo muutuja paevade_arv, mis näitab, mitu päeva reis kestab (integer)
# Loo muutuja oobimise_hind, mis näitab ühe öö hinna (float)
# Trüki välja lause, mis ühendab need andmed, nt: “Soome reis kestab 5 päeva ja üks öö maksab 30.50 eurot.”
# Kasuta väljatrükkimisel ainult komasid (,)

sihtkoht = "Haapsalu"
paevade_arv = 5
oobimise_hind = 100.50
kokku = paevade_arv * oobimise_hind
print(sihtkoht,"reis kestab", paevade_arv, "päeva ja maksab kokku",kokku,"€")

# harjutus 03.6
# Loo muutuja kylje_pikkus, mis määrab kujundi külje pikkuse (täisarv)
# Loo muutuja nurk, mis määrab kujundi nurga (täisarv)
# Loo muutuja kujundi_varv, mis määrab kujundi joonevärvi (string)
# Kasutades Turtle’i, joonista kõrvuti 3 värvilist ruutu, mis kasutab loodud muutujaid
# Iga ruut on järgmisest 1,5 korda eemal

kylje_pikkus = 100
nurk = 90
kujundi_varv = "blue"
x = 110

turtle.pencolor(kujundi_varv)
for j in range(3):
    for i in range(4):
        turtle.fd(kylje_pikkus)
        turtle.lt(nurk)
    turtle.penup()
    turtle.goto(x,0)
    turtle.pendown()
    x = x * 1.5
    print(x)



turtle.done()

#jea