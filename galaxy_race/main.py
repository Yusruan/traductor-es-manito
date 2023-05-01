import pygame, sys
from random import randint

pygame.init()

screen = pygame.display.set_mode((700, 500))
screen_dimensions = screen.get_size()

background = pygame.transform.scale(pygame.image.load("background.jpeg"), screen_dimensions)

obstacle_size = [100, 100]
obstacle = pygame.transform.scale(pygame.image.load("obstacle.png"), obstacle_size)

player_size = [100, 50]
player = pygame.transform.scale(pygame.image.load("player.png"), player_size)

player_position = [50, screen_dimensions[1]/2-player_size[1]/2]
obstacles = []

obstacle_creation = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_creation, 1000)

game_starttime = 0
died = False

font = pygame.font.SysFont("Arial", 20)
title = pygame.font.SysFont("Arial", 40)

game_over_title = title.render("Game over!", True, (255, 255, 255))
game_over_sub = font.render("press ENTER to restart", True, (255, 255, 255))

game_over_text = pygame.Surface((game_over_sub.get_width(), game_over_title.get_height() + game_over_sub.get_height()), pygame.SRCALPHA)
game_over_text.blit(game_over_title, (game_over_text.get_width()/2 - game_over_title.get_width()/2, 0))
game_over_text.blit(game_over_sub, (game_over_text.get_width()/2 - game_over_sub.get_width()/2, game_over_title.get_height()))


while True:

    if died:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                pygame.quit()
                sys.exit()
            
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:

                obstacles = []
                player_position = [50, screen_dimensions[1]/2-player_size[1]/2]
                game_starttime = round(pygame.time.get_ticks()/1000, 1)

                died = False

        screen.blit(background, (0, 0))
        screen.blit(game_over_text, (screen.get_width()/2-game_over_text.get_width()/2, screen.get_height()/2-game_over_text.get_height()/2))
        score_display = font.render("Score: "+str(score), True, (255, 255, 255))
        screen.blit(score_display, (screen.get_width()/2 - score_display.get_width()/2, screen.get_height()/2 - score_display.get_height()/2 + 100))
        
        pygame.display.update()
        pygame.time.Clock().tick(20)


    else:

        screen.blit(background, (0, 0))

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                pygame.quit()
                sys.exit()

            elif event.type == obstacle_creation:

                obstacles.append([screen_dimensions[0], randint(0, screen_dimensions[1]-obstacle_size[1])])

        if pygame.key.get_pressed()[pygame.K_DOWN] and player_position[1] <= screen_dimensions[1]-player_size[1] -5 :
            player_position[1] += 5
        if pygame.key.get_pressed()[pygame.K_UP] and player_position[1] >= 5:
            player_position[1] -= 5

        for obstacle_position in obstacles:

            obstacle_position[0] -= 10

            if -obstacle_size[0] +17 <= obstacle_position[0] - player_position[0] <= player_size[0] -17:
                if -obstacle_size[1] +17 <= obstacle_position[1] - player_position[1] <= player_size[1] -17:
                    
                    score = round(pygame.time.get_ticks()/1000 - game_starttime, 1)

                    died = True



            screen.blit(obstacle, obstacle_position)

        screen.blit(player, player_position)

        time = round(pygame.time.get_ticks()/1000 - game_starttime, 1)

        score_display = font.render("Time: "+str(time), True, (255, 255, 255))
        screen.blit(score_display, (0, 0))
        pygame.display.update()
        pygame.time.Clock().tick(60)
