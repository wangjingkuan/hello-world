import pygame
import random
import sys

# 游戏窗口大小
WIDTH, HEIGHT = 600, 400
BLOCK_SIZE = 20

# 颜色定义
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# 初始化pygame
pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('贪吃蛇 - 双食物版')
clock = pygame.time.Clock()
font = pygame.font.SysFont('Arial', 25)

def random_food(snake):
    while True:
        pos = [random.randrange(0, WIDTH, BLOCK_SIZE), random.randrange(0, HEIGHT, BLOCK_SIZE)]
        if pos not in snake:
            return pos

def main():
    snake = [[WIDTH // 2, HEIGHT // 2]]
    direction = 'RIGHT'
    change_to = direction
    score = 0

    # 初始化两个食物点
    food1 = random_food(snake)
    food2 = random_food(snake + [food1])

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != 'DOWN':
                    change_to = 'UP'
                elif event.key == pygame.K_DOWN and direction != 'UP':
                    change_to = 'DOWN'
                elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                    change_to = 'LEFT'
                elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                    change_to = 'RIGHT'

        direction = change_to
        head = snake[0][:]
        if direction == 'UP':
            head[1] -= BLOCK_SIZE
        elif direction == 'DOWN':
            head[1] += BLOCK_SIZE
        elif direction == 'LEFT':
            head[0] -= BLOCK_SIZE
        elif direction == 'RIGHT':
            head[0] += BLOCK_SIZE

        # 判断是否撞墙或撞到自己
        if (head[0] < 0 or head[0] >= WIDTH or head[1] < 0 or head[1] >= HEIGHT or head in snake):
            break

        snake.insert(0, head)
        ate_food = False
        if head == food1:
            score += 1
            food1 = random_food(snake + [food2])
            ate_food = True
        elif head == food2:
            score += 1
            food2 = random_food(snake + [food1])
            ate_food = True
        if not ate_food:
            snake.pop()

        window.fill(BLACK)
        for block in snake:
            pygame.draw.rect(window, GREEN, pygame.Rect(block[0], block[1], BLOCK_SIZE, BLOCK_SIZE))
        pygame.draw.rect(window, RED, pygame.Rect(food1[0], food1[1], BLOCK_SIZE, BLOCK_SIZE))
        pygame.draw.rect(window, BLUE, pygame.Rect(food2[0], food2[1], BLOCK_SIZE, BLOCK_SIZE))
        score_text = font.render(f'得分: {score}', True, WHITE)
        window.blit(score_text, (10, 10))
        pygame.display.flip()
        clock.tick(10)

    # 游戏结束
    window.fill(BLACK)
    game_over_text = font.render('游戏结束! 按任意键退出', True, WHITE)
    window.blit(game_over_text, (WIDTH // 2 - 120, HEIGHT // 2 - 20))
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
                pygame.quit()
                sys.exit()

if __name__ == '__main__':
    main()