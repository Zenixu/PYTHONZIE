
suhu = int(input("masukkan derajat suhu zat air: "))

if suhu <= 0:
    print (f"{suhu} ini adalah zat padat")
elif suhu >= 25:
    print (f"{suhu} ini adalah zat cair")
elif suhu >= 100:
    print (f"{suhu} ini adalah zat gas")