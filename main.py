import game

Game = game.SnakeGame()
    
while True:
    game_over, score = Game.play()

    if (game_over):
        break

print(f'Game over! Your score is {score}')

game.pygame.quit()