import qrcode

data = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

qr = qrcode.make(data)
qr.save("qrcode.png")

print("berhasil")