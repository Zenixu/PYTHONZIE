J1 = int(input("masukan waktu Jam pertama dalam bentuk detik: "))
J2 = int(input("masukan waktu Jam Kedua dalam bentuk detik: "))

jam1 = int(J1 / 3600)
J1 = J1 % 3600
menit1 = int(J1 / 60)
J1 = J1 % 60
total_detik1 = (jam1 * 3600) + (menit1 * 60) + J1

jam2 = int(J2 / 3600)
J2 = J2 % 3600
menit2 = int(J2 / 60)
J2 = J2 % 60
total_detik2 = (jam2 * 3600) + (menit2 * 60) + J2

J3 = int (J2 - J1)

jam3 = int(jam2 - jam1)
J3 = J3 % 3600
menit3 = int(menit2 / menit1)
J3 = J3 % 60

print (f"{jam1}/{menit1}/{J1}       {jam2}/{menit2}/{J2}       {jam3}/{menit3}/{J3}")
