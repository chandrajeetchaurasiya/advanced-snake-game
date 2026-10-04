import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen settings
WIDTH = 600
HEIGHT = 400

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
RED = (255, 0, 0)

# Snake settings
BLOCK_SIZE = 20
snake = [(300, 200), (280, 200), (260, 200)]

direction = "RIGHT"

# Food
food = (
    random.randrange(0, WIDTH, BLOCK_SIZE),
    random.randrange(0, HEIGHT, BLOCK_SIZE)
)

# Game speed
clock = pygame.time.Clock()
SPEED = 10

# Font
font = pygame.font.SysFont("Arial", 25)


def draw_snake():
    for x, y in snake:
        pygame.draw.rect(
            screen,
            GREEN,
            (x, y, BLOCK_SIZE, BLOCK_SIZE)
        )


def draw_food():
    pygame.draw.rect(
        screen,
        RED,
        (food[0], food[1], BLOCK_SIZE, BLOCK_SIZE)
    )


def show_game_over():
    message = font.render(
        "Game Over! Press R to restart or Q to quit",
        True,
        WHITE
    )

    screen.blit(
        message,
        (
            WIDTH // 2 - message.get_width() // 2,
            HEIGHT // 2 - message.get_height() // 2
        )
    )

    pygame.display.update()


def new_food():
    while True:
        new_position = (
            random.randrange(0, WIDTH, BLOCK_SIZE),
            random.randrange(0, HEIGHT, BLOCK_SIZE)
        )

        if new_position not in snake:
            return new_position


running = True
game_over = False

while running:

    # Handle events
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_UP and direction != "DOWN":
                direction = "UP"

            elif event.key == pygame.K_DOWN and direction != "UP":
                direction = "DOWN"

            elif event.key == pygame.K_LEFT and direction != "RIGHT":
                direction = "LEFT"

            elif event.key == pygame.K_RIGHT and direction != "LEFT":
                direction = "RIGHT"

            elif game_over and event.key == pygame.K_r:
                snake = [
                    (300, 200),
                    (280, 200),
                    (260, 200)
                ]

                direction = "RIGHT"
                food = new_food()
                game_over = False

            elif game_over and event.key == pygame.K_q:
                running = False

    if not game_over:

        # Current snake head
        head_x, head_y = snake[0]

        # Move snake
        if direction == "UP":
            head_y -= BLOCK_SIZE

        elif direction == "DOWN":
            head_y += BLOCK_SIZE

        elif direction == "LEFT":
            head_x -= BLOCK_SIZE

        elif direction == "RIGHT":
            head_x += BLOCK_SIZE

        new_head = (head_x, head_y)

        # Wall collision
        if (
            head_x < 0
            or head_x >= WIDTH
            or head_y < 0
            or head_y >= HEIGHT
        ):
            game_over = True

        # Self collision
        elif new_head in snake:
            game_over = True

        else:
            snake.insert(0, new_head)

            # Food collision
            if new_head == food:
                food = new_food()

            else:
                snake.pop()

        # Draw everything
        screen.fill(BLACK)

        draw_snake()
        draw_food()

        pygame.display.update()

        clock.tick(SPEED)

    else:
        screen.fill(BLACK)
        draw_snake()
        draw_food()
        show_game_over()


pygame.quit()
sys.exit()