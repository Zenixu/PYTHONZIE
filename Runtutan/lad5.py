#Konversi suhu 
while True:
    print ("====Konversi Suhu====")
    C = float(input("Masukkan Suhu Celcius: "))

    F = 9/5 * C + 32
    K = C + 273
    R = C * 4/5

    print ("=============================")
    print (f"{C} 'Derajat celcius' = {F} Derajat Fahrenheit")
    print ("=============================")
    print (f"{C} 'Derajat celcius' = {K} Derajat Kelvin")
    print ("=============================")
    print (f"{C} 'Derajat celcius' = {R} Derajat Reamur\n")