import random
print("Selamat Datang di Coinflipz")

choice=input("Kamu pilih sisinya (heads or tails): ").lower()

num=random.randint(1,2)
if num==1:
    result="heads"
    
elif num==2:
    result="tails"

if choice==result:
    print("Busett kamu wangii banget kang, Selamat Anda Menang. The coin flipped ", result)
else:
    print("Bau banget kang aduhhh..., Nice try kamu kalah. The coin flipped ", result)
print("MAKASIH YAA UDAH MAININNN")