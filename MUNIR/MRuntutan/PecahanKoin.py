PECAHAN = [1000, 500, 100, 50, 25]

uang = int(input("masukan nilai uang: "))
pecahan_1000 = int(uang/1000)
uang = uang % 1000
pecahan_500 = int(uang/500)
uang = uang % 500
pecahan_100 = int(uang/100)
uang = uang % 100
pecahan_50 = int(uang/50)
uang = uang % 50
pecahan_25 = int(uang/25)
uang = uang % 25

print (f'''Terdiri dari: 
{pecahan_1000} Pecahan uang Rp.1000 
{pecahan_500} Pecahan uang Rp.500  
{pecahan_100} Pecahan uang Rp.100  
{pecahan_50} Pecahan uang Rp.50  
{pecahan_25} Pecahan uang Rp.25 ''')