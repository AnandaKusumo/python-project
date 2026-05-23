mode = input("Text/Biner: ")

if mode.lower() == "teks":
    teks = input("masukkan Teks: ")
    hasil = ' '.join(format(ord(h), '08b') for h in teks)
    print(hasil)

elif mode.lower() == "biner":
    biner = input("Masukkan Biner: ")
    hasil = ''.join(chr(int(b, 2)) for b in biner.split())
    print(hasil)
