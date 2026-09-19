detik = int(input("masukan lama percakapan dalam detik: "))

jam = int(detik / 3600)
detik = detik % 3600
menit = int(detik / 60)
detik = detik % 60
total_detik = (jam * 3600) + (menit * 60) + detik

print (f'''lama percakapan anda adalah 
{total_detik} detik
{jam} jam 
{menit} menit 
{detik} detik
{jam}/{menit}/{detik}
''')