LOGO = """
░██╗░░░░░░░██╗███████╗██╗░░░░░░█████╗░░█████╗░███╗░░░███╗███████╗  ████████╗░█████╗░  ██╗░░██╗███████╗██╗░░░░░██╗░░░░░
░██║░░██╗░░██║██╔════╝██║░░░░░██╔══██╗██╔══██╗████╗░████║██╔════╝  ╚══██╔══╝██╔══██╗  ██║░░██║██╔════╝██║░░░░░██║░░░░░
░╚██╗████╗██╔╝█████╗░░██║░░░░░██║░░╚═╝██║░░██║██╔████╔██║█████╗░░  ░░░██║░░░██║░░██║  ███████║█████╗░░██║░░░░░██║░░░░░
░░████╔═████║░██╔══╝░░██║░░░░░██║░░██╗██║░░██║██║╚██╔╝██║██╔══╝░░  ░░░██║░░░██║░░██║  ██╔══██║██╔══╝░░██║░░░░░██║░░░░░
░░╚██╔╝░╚██╔╝░███████╗███████╗╚█████╔╝╚█████╔╝██║░╚═╝░██║███████╗  ░░░██║░░░╚█████╔╝  ██║░░██║███████╗███████╗███████╗
░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚══════╝  ░░░╚═╝░░░░╚════╝░  ╚═╝░░╚═╝╚══════╝╚══════╝╚══════╝
"""

class Player:
    def __init__(self):
        self.life = 3
        self.items = []

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

    room = select_input("What room will you enter", 
        a = "Plesant looking room",
        b = "Room covered in blood"
    )

    match room:
        case "a": return pleasant_room(player)
        case "b": return

def pleasant_room(player: Player):
    room = select_input("What will you use against a ZOMBIE ??", 
        a = "gun a",
        b = "gun b"
    )

if __name__ == "__main__":
    print(LOGO)

    player = Player()
    welcome_room(player = player)