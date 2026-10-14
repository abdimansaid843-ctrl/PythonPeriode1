#opdracht 1
print("opdracht 1")

age = 17

if age >= 18:
    print("Je bent volwassen.")
else:
    print("Je bent nog geen 18.")
print()


#opdracht 2
print("opdracht 2")

grade = 7.5

if grade >= 5.5:
    print("Je hebt een voldoende!")
else:
    print("Je hebt een onvoldoende.")
print()


#opdracht 3
print("opdracht 3")

grade = 4

if grade >= 8:
    print("Goed gedaan!")
elif grade >= 5.5:
    print("Voldoende!")
else:
    print("Onvoldoende.")
print()


#opdracht 4
print("opdracht 4")

health = 75
has_shield = True

if health >= 50:
    print("Je hebt genoeg health.")
else:
    print("Je hebt weinig health!")

if has_shield:
    print("Je hebt een schild!")
print()


#opdracht 5
print("opdracht 5")

age = 17
has_ticket = True

if age >= 18 and has_ticket:
    print("Je mag naar binnen!")
else:
    print("Je mag niet naar binnen.")
print()


#opdracht 6
print("opdracht 6")

for getal in range(1, 11):
    print(getal)
print()


#opdracht 7
print("opdracht 7")

for getal in range(1, 11):
    print(f"{getal} x 5 = {getal * 5}")
print()


#opdracht 8
print("opdracht 8")

countdown = 10

while countdown > 0:
    print(countdown)
    countdown -= 1

print("GO!")
print()


#opdracht 9
print("opdracht 9")

health = 100

for i in range(5):
    health -= 20
    print("Health:", health)
print()


#opdracht 10
print("opdracht 10")

for getal in range(1, 11):
    if getal % 2 == 0:
        print(getal, "is even")
    else:
        print(getal, "is oneven")
print()


#opdracht 11
print("opdracht 11")

for vijand in range(1, 6):
    print(f"vijand {vijand}")

    enemy_health = 30

    while enemy_health > 0:
        enemy_health -= 10
        print("vijand health:", enemy_health)

    print("Vijand verslagen!")
print()


#eindopdracht
print("eindopdracht player training")

player_name = "abdi"
level = 1
experience = 0
damage = 10

for training in range(1, 11):
    experience += 20
    print(f"{player_name} heeft nu {experience} experience.")

    if experience >= 100:
        level += 1
        damage += 5
        experience = 0
        print("LEVEL UP!")

print("Training voltooid!")
print("Level:", level)
print("Experience:", experience)
print("Damage:", damage)
