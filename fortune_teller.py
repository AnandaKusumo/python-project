import random
import datetime

print("=== Today's Fortune!!! ===")

hari = datetime.datetime.now().strftime("%A")

luck = random.randint(1, 100)

if hari == "Friday":
    print("Golden Day!")
    luck *= 2

elif hari == "Monday":
    luck -= 20

event = random.randint(1, 20)

if event == 1:
    print("Fortuna just blessed you")
    luck += 100

elif event == 2:
    print("Gah dayum gng, you got cursed💔💔")
    luck -= 67

if luck < 0:
    luck = 0

print(f"\n Your luck is: {luck}\n")

fortune = [
    "Sunshine and Rainbows",
    "Four-leaf clover on your pocket",
    "The atoms decided to be good",
    "Smooth day"
]

misfortune = [
    "Bad day",
    "Hell",
    "Hellish Hell",
    "Nightmarish Hellish Hell",
    "Cursed by Fortuna"
]

if luck >= 150:
    print("Fortuna is on your side")

elif luck <= 20:
    print(random.choice(misfortune))

elif luck <= 40:
    print("Just an ordinary days, i guess")

else:
    print(random.choice(fortune))

rare = random.randint(1, 1000)

if rare == 777:
    print("JACKPOt!!!")