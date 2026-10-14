print("opdracht-1")
age = int(input("Hoe oud ben je? "))

if age >= 18:
    print("Je bent volwassen.")
else:
    print("Je bent nog geen 18.")

print()
print("opdracht-2")
grade = float(input("Wat is je cijfer? "))

if grade >= 5.5:
    print("Je hebt een voldoende behaald.")
else:
    print("Je hebt geen voldoende behaald.")



print()
print("opdracht-3")
grade1 = float(input("Wat is je cijfer? "))

if grade1 >= 8:
    print("Goed gedaan!")
elif grade1 >= 5.5:
    print("Voldoende!")
else:
    print("Onvoldoende.")

print()
print("opdracht-4")
health= 75
dammage = float(input("hoeveel schade heb je opgelopen? "))

health -= dammage
has_shield= True

print("Je health is", health)
if health <=50:
    print("je hebt nu!", health, "health over")

print()
print("opdracht-5")
age= int(input("Wat is je leeftijd? "))
has_ticket= input("Heb je een ticket? (ja/nee) ")
if has_ticket.lower() == "ja" and age >= 18:
    print("Je mag naar binnen.")
else:
    print("Je mag niet naar binnen.")

print()
print("opdracht-6")
for i in range(1, 11):
    print(i)

print()
print("opdracht-7")
for getal in range(1, 11):
    print(f"{getal} x 5 = {getal * 5}")

print()
print("opdracht-8")
for getal in range(11, 1, -1):
    print(f"{getal-1}")
    
print("go!")

print()
print("of")
countdown = 10

while countdown > 0:
    print(countdown)
    countdown -= 1

print("GO!")
