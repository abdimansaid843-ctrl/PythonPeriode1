#weapon selector
print("weapon selector")
print()

#stap 1
player_name = "abdi"
selected_weapon = "sword"
weapon_damage = 0

#stap 2
match selected_weapon:
    case "sword":
        weapon_damage = 20
        print("Je gebruikt een zwaard!")
    case "bow":
        weapon_damage = 15
        print("Je gebruikt een boog!")
    case "staff":
        weapon_damage = 25
        print("Je gebruikt een magische staf!")
    case "axe":
        weapon_damage = 30
        print("Je gebruikt een bijl!")
    #bonus 1
    case "dagger":
        weapon_damage = 10
        print("Je gebruikt een dolk!")
    case "hammer":
        weapon_damage = 35
        print("Je gebruikt een enorme hamer!")
    case _:
        weapon_damage = 0
        print("Onbekend wapen!")

#stap 3
print()
print(f"Speler: {player_name}")
print(f"Wapen: {selected_weapon}")
print(f"Damage: {weapon_damage}")

#bonus 2
enemy_health = 100

print()
for aanval in range(1, 4):
    enemy_health -= weapon_damage
    if enemy_health < 0:
        enemy_health = 0
    print(f"Aanval {aanval}: de vijand heeft nog {enemy_health} health")

#bonus 3
print()
while enemy_health > 0:
    enemy_health -= weapon_damage
    if enemy_health < 0:
        enemy_health = 0
    print(f"De vijand heeft nog {enemy_health} health")

print("Vijand verslagen!")
