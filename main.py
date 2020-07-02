from player import Player

def game_run():
    is_user_playing = True
    while is_user_playing is True:
        player_name = input("what is ur name:\n").lower()
        player_class = input("Choose your class.\nMage, Thief, or Warrior:\n").lower()
        while player_class not in ("mage", "thief", "warrior"):
            print("sorry, please type \"Mage\", \"Thief\", or \"Warrior\"")
            player_class = input("Choose your class.\n Mage, Thief, Warrior")
        print("you have selected", player_class)
        print(player_name, player_class)
        player = Player(player_name, player_class)
        break



game_run()
