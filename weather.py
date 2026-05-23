import requests

API_KEY = "244a48f946ea67dc3fcc2ba18589bfdb"

kota = input("Masukkan Nama Kota: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={kota}&appid={API_KEY}&units=metric"

data = requests.get(url).json()

if data.get("cod") == 200:
    suhu = data["main"]["temp"]
    cuaca = data["weather"][0]["description"]
    kelembapan = data["main"]["humidity"]
else:
    print("Kota tidak ditemukan!")
    exit()

print("\n=== Weather Report ===")
print(f"Kota            : {kota}")
print(f"Suhu            : {suhu}°C")
print(f"Cuaca           : {cuaca}")
print(f"Kelembapan      : {kelembapan}")