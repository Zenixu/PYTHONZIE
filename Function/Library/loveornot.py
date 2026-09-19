import random
print ("====Apakah dia menyukai mu?=====")
while True:
    urname = (input("Siapa nama kamu?: "))
    nama = str(input("Masukan nama orang yang di sukai: "))
    test = ("Apakah dia mencintai mu?: ")
    acak = (random.randint (1,3))
    
    print ("=============================") 
    print (f"nama saya adalah: {urname}")
    print (f"nama orang yang saya sukai : {nama}\n")

    if  acak == (1):
        print(f"selamat {nama} menyukaimu, langsung tembak aja ga sie")
        print ("======================================================\n")
    else:
        acak <= (2)
        print (f"utututu sedih banget {nama} tidak mencintai kamu {urname}, {urname} NT wakakaka")
        print ("======================================================\n")
    