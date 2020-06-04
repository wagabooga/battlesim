from player import Player


def game_run():
    is_user_playing = True
    while is_user_playing is True:
        player_name = input("what is ur name")
        player = Player(player_name)
        print(player.name)
        return player.name


game_run()