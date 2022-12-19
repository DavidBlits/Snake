import pygame
import random
def main(*args):
    pygame.init()
    clock=pygame.time.Clock()
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Snake")
    snake = [(200, 200), (210, 200), (220, 200)]
    snake_skin = pygame.Surface((10, 10))
    snake_skin.fill((255, 255, 255))
    apple=(random.randint(0, 63)*10, random.randint(0, 47)*10)
    apple_skin = pygame.Surface((10, 10))
    apple_skin.fill((255, 0, 0))
    my_direction = None
    tick=10
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_UP,pygame.K_w] and my_direction != "down":
                    snake.append((snake[-1][0], snake[-1][1] - 10))
                    snake.pop(0)
                    my_direction = "up"
                if event.key in [pygame.K_RIGHT,pygame.K_d] and my_direction != "left":
                    snake.append((snake[-1][0]+10, snake[-1][1]))
                    snake.pop(0)
                    my_direction = "right"
                if event.key in [pygame.K_DOWN,pygame.K_s] and my_direction != "up":
                    snake.append((snake[-1][0], snake[-1][1] +10))
                    snake.pop(0)
                    my_direction = "down"
                if event.key in [pygame.K_LEFT,pygame.K_a] and my_direction != "right":
                    snake.append((snake[-1][0]-10, snake[-1][1]))
                    snake.pop(0)
                    my_direction = "left"
        if my_direction:    
            if my_direction == "up":
                snake.append((snake[-1][0], snake[-1][1] - 10))
                snake.pop(0)
            if  my_direction == "right":
                snake.append((snake[-1][0]+10, snake[-1][1]))
                snake.pop(0)
            if my_direction == "down":
                snake.append((snake[-1][0], snake[-1][1] +10))
                snake.pop(0)
            if my_direction == "left":
                snake.append((snake[-1][0]-10, snake[-1][1]))
                snake.pop(0)
                
        if snake[-1][0] > 640 or snake[-1][0] < 0 or snake[-1][1] > 480 or snake[-1][1] < 0:
            pygame.quit()
            
        if snake[-1] == apple:
            apple=(random.randint(0, 63)*10, random.randint(0, 47)*10)
            snake.insert(0, snake[0])
            tick+=1
            
        screen.fill((0, 0, 0))
        for pos in snake:
            screen.blit(snake_skin, pos)
        screen.blit(apple_skin, apple)
        pygame.display.update()
        clock.tick(tick)
if __name__ == '__main__':
    main()
    
