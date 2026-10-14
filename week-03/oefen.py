#oefening 1
print("oefening 1")

books = ["harry potter", "de hobbit", "1984", "animal farm", "the great gatsby"]

for book in books:
    print(book)
print()


#oefening 2
print("oefening 2")

games = ["minecraft", "fortnite", "roblox", "fifa", "call of duty"]

for game in games:
    print(f"Ik speel graag {game}")
print()


#oefening 3
print("oefening 3")

scores = [10, 25, 40, 15, 30]

for score in scores:
    print(score)
    nieuwe_score = score + 10
    print(f" nieuwe score: {nieuwe_score}")
print()


#oefening 4
print("oefening 4")

for getal in range(1, 11):
    print(getal)
print()


#oefening 5
print("oefening 5")

for getal in range(1, 11):
    print(f"{getal} x 5 = {getal * 5}")
print()


#oefening 6
print("oefening 6")

countdown = 10

while countdown > 0:
    print(countdown)
    countdown -= 1

print("START!")
print()


#oefening 7
print("oefening 7")

monsterHealth = 100
damage = 20

while monsterHealth > 0:
    monsterHealth -= damage
    print(f"monster health: {monsterHealth}")

print("Monster verslagen!")
print()


#oefening 8
print("oefening 8")

inventory = ["sword", "potion", "shield", "bow", "key"]

itemCount = 0

for item in inventory:
    print(item)
    itemCount += 1

    if item == "potion":
        print("Deze potion geeft health terug")
    elif item == "key":
        print("Met deze key kun je een deur openen")

print(f"Totaal aantal items: {itemCount}")
