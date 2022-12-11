import random

LOGO = """
░██╗░░░░░░░██╗███████╗██╗░░░░░░█████╗░░█████╗░███╗░░░███╗███████╗  ████████╗░█████╗░  ██╗░░██╗███████╗██╗░░░░░██╗░░░░░
░██║░░██╗░░██║██╔════╝██║░░░░░██╔══██╗██╔══██╗████╗░████║██╔════╝  ╚══██╔══╝██╔══██╗  ██║░░██║██╔════╝██║░░░░░██║░░░░░
░╚██╗████╗██╔╝█████╗░░██║░░░░░██║░░╚═╝██║░░██║██╔████╔██║█████╗░░  ░░░██║░░░██║░░██║  ███████║█████╗░░██║░░░░░██║░░░░░
░░████╔═████║░██╔══╝░░██║░░░░░██║░░██╗██║░░██║██║╚██╔╝██║██╔══╝░░  ░░░██║░░░██║░░██║  ██╔══██║██╔══╝░░██║░░░░░██║░░░░░
░░╚██╔╝░╚██╔╝░███████╗███████╗╚█████╔╝╚█████╔╝██║░╚═╝░██║███████╗  ░░░██║░░░╚█████╔╝  ██║░░██║███████╗███████╗███████╗
░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚══════╝  ░░░╚═╝░░░░╚════╝░  ╚═╝░░╚═╝╚══════╝╚══════╝╚══════╝
"""

# player or enemy or gun
class Item:
    def __init__(self, name: str, life: int):
        self.name = name
        self.life = life

    def __str__(self):
        return self.name

class Player(Item):
    def __init__(self, name: str, life: int):
        super().__init__(name, life)

        self.guns = []

    def select_gun(self):
        i = select_input("Select your weapon", **{str(i): str(gun) for i, gun in enumerate(self.guns)})
        return int(i)

    def fight_enemy(self, enemy, gun):
        starts = random.randint(0, 1)
        
        while player.life > 0 and enemy.life > 0:
            if starts:
                self.guns[gun].use(enemy)
                enemy.gun.use(player)
            else:
                enemy.gun.use(player)
                self.guns[gun].use(enemy)

        return not self.life <= 0

class Enemy(Item):
    def __init__(self, name: str, life: int, gun):
        super().__init__(name, life)

        self.gun = gun

class Gun(Item):
    def __init__(self, name: str, life: int, damage: int):
        super().__init__(name, life)

        self.damage = damage

    def use(self, enemy):
        self.life -= 1
        enemy.life -= self.damage

    def __str__(self):
        return f"{self.name}: damage -> {self.damage} life -> {self.life}"

def select_input(question: str, line : bool = True, **kwargs):
    if line:
        print("\n-------------------------")
    
    print(question)

    for k, v in kwargs.items():
        print(f"{k}.) {v}.")
    
    while True:
        output = input(": ")
        if output in kwargs.keys():
            return output

def welcome_room(player: Player):
    print("Demons have atacked your base")
    print("Your friends are death")
    print("KILL THAM ALL AND SURVIVE")

    gun = select_input("Select your gun", 
        a = "AKA...", 
        b = "banana"
    )

    match gun:
        case "a": player.guns.append(Gun("Aka...", 4, 2))
        case "b": player.guns.append(Gun("Banana", 6, 1))

    room = select_input("What room will you enter", 
        a = "Plesant looking room",
        b = "Room covered in blood"
    )

    match room:
        case "a": return pleasant_room(player)
        case "b": return

def pleasant_room(player: Player):
    enemy_gun = Gun(name = "aka", life = 2, damage = 3)
    enemy = Enemy(name = "MonkeySpider", life = 2, gun = enemy_gun)
    
    player_won = player.fight_enemy(enemy, gun = player.select_gun())
    if not player_won:
        return lose_room(player, enemy)
    
    return win_room(player)

def lose_room(player: Player, killed_by = None):
    print("End of game")
    
    if killed_by != None:
        print(f"You were killed by {killed_by} with gun {killed_by.gun}")

def win_room(player: Player):
    print("U WON NIGGA")

if __name__ == "__main__":
    print(LOGO)

    player = Player(name = input("NAME: "), life = 5)
    welcome_room(player = player)