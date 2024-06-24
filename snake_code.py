import pygame
import sys
import random
from pygame.locals import *

# Initialize Pygame
pygame.init()

# Constants
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 400
GRID_SIZE = 20
GRID_WIDTH = WINDOW_WIDTH // GRID_SIZE
GRID_HEIGHT = WINDOW_HEIGHT // GRID_SIZE
GAME_SPEED = 10  # Snake movement speed
RED_SNAKE_DURATION = 15 * 1000  # 15 seconds in milliseconds
INVERT_CONTROLS_DURATION = 10 * 1000  # 10 seconds in milliseconds
BLUE_RAT_DURATION = 10 * 1000  # 10 seconds in milliseconds
NORMAL_RAT_POINTS = 5
BLUE_RAT_POINTS = 20

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Directions
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Snake class
class Snake:
    def __init__(self, color, initial_position):
        self.color = color
        self.positions = [initial_position]
        self.direction = RIGHT
        self.grow = False

    def get_head_position(self):
        return self.positions[0]

    def turn(self, point):
        if self.positions[1] != (self.get_head_position()[0] + point[0], self.get_head_position()[1] + point[1]):
            self.direction = point

    def move(self):
        cur = self.get_head_position()
        x, y = self.direction
        new = (((cur[0] + (x * GRID_SIZE)) % WINDOW_WIDTH), (cur[1] + (y * GRID_SIZE)) % WINDOW_HEIGHT)
        if len(self.positions) > 2 and new in self.positions[2:]:
            self.reset()
        else:
            self.positions.insert(0, new)
            if len(self.positions) > 1 and not self.grow:
                self.positions.pop()
            else:
                self.grow = False

    def reset(self):
        self.positions = [(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)]
        self.direction = RIGHT

    def draw(self, surface):
        for p in self.positions:
            r = pygame.Rect((p[0], p[1]), (GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(surface, self.color, r)
            pygame.draw.rect(surface, WHITE, r, 1)

    def collision_with_food(self, food_position):
        if self.get_head_position() == food_position:
            self.grow = True
            return True
        return False

# Food class
class Food:
    def __init__(self):
        self.position = (0, 0)
        self.color = GREEN
        self.randomize_position()

    def randomize_position(self):
        self.position = (random.randint(0, GRID_WIDTH - 1) * GRID_SIZE, random.randint(0, GRID_HEIGHT - 1) * GRID_SIZE)

    def draw(self, surface):
        r = pygame.Rect((self.position[0], self.position[1]), (GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(surface, self.color, r)
        pygame.draw.rect(surface, WHITE, r, 1)

# Main function
def main():
    global RED_SNAKE_DURATION, INVERT_CONTROLS_DURATION, BLUE_RAT_DURATION, NORMAL_RAT_POINTS, BLUE_RAT_POINTS

    # Initialize variables
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)
    pygame.display.set_caption('Snake Game')
    surface = pygame.Surface(window.get_size())
    surface = surface.convert()

    snake = Snake(RED, (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
    food = Food()

    red_snake_timer = 0
    red_snake_active = False
    invert_controls_timer = 0
    invert_controls_active = False
    blue_rat_timer = 0
    blue_rat_active = False
    score = 0
    game_over = False

    clock = pygame.time.Clock()

    # Game loop
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_UP:
                    snake.turn(UP)
                elif event.key == K_DOWN:
                    snake.turn(DOWN)
                elif event.key == K_LEFT:
                    snake.turn(LEFT)
                elif event.key == K_RIGHT:
                    snake.turn(RIGHT)

        # Check if red snake appears
        current_time = pygame.time.get_ticks()
        if current_time - red_snake_timer > RED_SNAKE_DURATION:
            red_snake_timer = current_time
            red_snake_active = True

        # Check if red snake hits the snake head
        if red_snake_active:
            # Logic for red snake movement and collision
            pass  # Placeholder for red snake logic

        # Check if invert controls is active
        if invert_controls_active:
            # Logic to handle inverted controls
            pass  # Placeholder for invert controls logic

        # Check if blue rat appears
        if current_time - blue_rat_timer > BLUE_RAT_DURATION:
            blue_rat_timer = current_time
            blue_rat_active = True

        # Move snake
        snake.move()

        # Check for collision with food
        if snake.collision_with_food(food.position):
            score += NORMAL_RAT_POINTS
            food.randomize_position()

        # Draw everything
        surface.fill(BLACK)
        snake.draw(surface)
        food.draw(surface)
        window.blit(surface, (0, 0))
        pygame.display.update()

        clock.tick(GAME_SPEED)

if __name__ == '__main__':
    main()
