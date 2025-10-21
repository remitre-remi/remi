
# 01
# Koosta programm, mis kontrollib, kas kasutaja poolt sisestatud arv on paaris või paaritu
# kuvatakse korrektne arusaadav küsimus ja vastus - 1p
# eelnev kontroll, kas kasutaja ei lisanud arvu või pani nulli - 1p
# kood mis teavitab paaris või paaritust arvust - 1p
# kuvatakse programmi pealkiri - 1p
# kood kommenteeritud - 1p

print("=====ARVU KONTROLL!=====")

try:
    arv = int(input("Kontrolli arvu: "))
    
    valem = arv % 2
    if valem == 0:
        print("see on paarisarv")
    else:
        print("see on paaritu arv")
       
except:
    print("Miskit läks nihu!")