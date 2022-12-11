vsetky objekty hre ako nepriatel alebo hrac musia mat nazov

ked chceme vytvorit zbran:
    gun = Gun(name = "Banana", life = 4, damage = 5)

    zbran sa bude volat "Banana" ma 4 naboje (life idk why) a jeden naboj ubere nepriatelovi 5

ked chceme vytovit nepriatela:
    enemy_gun = Gun(name = "Banana", life = 4, damage = 5)
    enemy = Enemy(name = "name", life = 3, gun = enemy_gun)

    nepriatel musi mat aj zbran

ked chceme vybrat moznost:
    gun = select_input("Select your gun", 
        a = "AKA...", 
        b = "banana"
    )

    match gun:
        case "a": player.guns.append(Gun("Aka...", 4, 2)) # name, life, damage
        case "b": player.guns.append(Gun("Banana", 6, 1))

    tymto pridama novu zbran pouzivatelovi

    ---------------------------

    room = select_input("What room will you enter", 
        a = "Plesant looking room",
        b = "Room covered in blood"
    )

    match room:
        case "a": return pleasant_room(player)
        case "b": return

    tymto vybereme novu izbu

ked chceme presmerovat do inej izby
    return new_room(player)

novu izbu spravime

def new_room(player):
    print(player.name)

    return win_room(player) # tu zmenime na vlastny smer