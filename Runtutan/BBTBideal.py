tb = int(input("masukan tinggi badan dalam bentuk cm: "))

bb_ideal = tb - 100
bb_ideal -= int(0.1 * bb_ideal)

print (f"tinggi badan anda adalah {tb}cm dan berat badan ideal untuk anda adalah {bb_ideal}Kg")