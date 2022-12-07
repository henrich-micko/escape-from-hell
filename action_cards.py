
class FullPackBackException(Exception):
    def __init__(self):
        super().__init__("PackBack is full")

class GunNotFoundException(Exception):
    def __init__(self):
        super().__init__("Item not found")

class Enemy:
    def __init__(self, life, name):
        self.life = life
        self.name = name

class Gun:
    def __init__(self, damage, size, name):
        self.damage = damage
        self.size = size
        self.name = name

class Player:
    def __init__(self, packback_size = 10, life = 3):
        self._packback = []
        self._packback_size = packback_size
        self._life = life

    def add_to_packback(self, gun: Gun):
        packback_sum = sum([i.size for i in self._packback]) + gun.size
        if packback_sum > self._packback_size:
            raise FullPackBackException()

        self._packback.append(gun)

    def remove_from_packback(self, gun: Gun):
        if not gun in self._packback:
            raise GunNotFoundException()

        self._packback.remove(gun)
    
    def packback_input(self):
        for i, item in enumerate(self._packback):
            print(f"{i}: {item.name}")
        print("Vyber zbraň")
        id = int(input(""))
        output = self._packback[id]
        self.remove_from_packback(output)
        return output

class ActionCard:
    def __init__(self, player: Player):
        self.player = player

    def run(self):
        return None

class HellCard(ActionCard):
    def run(self):
        self.player.packback_input()
        return HellCard

def start_game_on_card(player, card):
    card_output = card(player = player).run()
    if card_output == None:
        return
    start_game_on_card(player, card_output)

player = Player()
player.add_to_packback(Gun(5, 5, 1))

start_game_on_card(player, HellCard)