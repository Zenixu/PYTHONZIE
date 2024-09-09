lama_percakapan = int(input("masukan lama percakapan dalam detik: "))

jam = int(lama_percakapan / 3600)
lama_percakapan = lama_percakapan % 3600
menit = int(lama_percakapan / 60)
lama_percakapan = lama_percakapan % 60

print (f"lama percakapan anda adalah {jam} jam {menit} menit {lama_percakapan} detik")