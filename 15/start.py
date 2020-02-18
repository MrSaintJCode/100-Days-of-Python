import pygame

# Learning PyGame From:
# https://www.youtube.com/watch?v=FfWpgLFMI7w

# Screen Size
screen = pygame.display.set_mode((800,600))

# Panel 
game_name = "Space Invaders"
game_icon = "sprites/icon.png"

# Game Images
player_image = "sprites/Player.png"


def main():

    # Game - Title and Icon
    pygame.display.set_caption(game_name)

    icon = pygame.image.load(game_icon)
    pygame.display.set_icon(icon)

    # Player
    player_x_pos = 370
    player_y_pos = 480
    player_spaceship = pygame.image.load(player_image)

    def player():
        screen.blit(player_spaceship,(player_x_pos,player_y_pos))


    # Game Loop
    game_on = True
    print("")
    print("-- Starting Game Loop --")
    while game_on:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_on = False

        # Background
        screen.fill((0, 0, 0))

        player()

        pygame.display.update()

if __name__ == '__main__':
    try:
        # Game - INIT
        pygame.init()
        main()  
    except (KeyboardInterrupt) as reason:
        print("")
        print("---- Game Closed ----")
        print(reason)