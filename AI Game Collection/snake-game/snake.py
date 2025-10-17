import pygame
import random
import heapq

# Initialize Pygame
pygame.init()
WIDTH, HEIGHT = 600, 600
CELL_SIZE = 24
GRID = WIDTH // CELL_SIZE

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake + A* AI")
clock = pygame.time.Clock()

# Colors
BG_COLOR = (10, 15, 25)
SNAKE_COLOR = (30, 180, 250)
BODY_COLOR = (25, 60, 110)
FOOD_COLOR = (255, 90, 90)
TEXT_COLOR = (200, 255, 220)

# Game variables
snake = []
direction = (1, 0)
food = (0, 0)
ai_enabled = False
score = 0


def reset():
    global snake, direction, food, ai_enabled, score
    snake = [(GRID // 2, GRID // 2)]
    direction = (1, 0)
    ai_enabled = False
    score = 0
    place_food()


def place_food():
    global food
    while True:
        food = (random.randint(0, GRID - 1), random.randint(0, GRID - 1))
        if food not in snake:
            return


def draw():
    screen.fill(BG_COLOR)
    # Food
    fx, fy = food
    pygame.draw.rect(screen, FOOD_COLOR, (fx * CELL_SIZE + 4, fy * CELL_SIZE + 4, CELL_SIZE - 8, CELL_SIZE - 8))

    # Snake
    for i, (x, y) in enumerate(snake):
        color = SNAKE_COLOR if i == 0 else BODY_COLOR
        pygame.draw.rect(screen, color, (x * CELL_SIZE + 2, y * CELL_SIZE + 2, CELL_SIZE - 4, CELL_SIZE - 4))

    # Score
    font = pygame.font.SysFont("Arial", 24)
    text = font.render(f"Score: {score} {'(AI)' if ai_enabled else ''}", True, TEXT_COLOR)
    screen.blit(text, (10, 10))
    pygame.display.flip()


def neighbors(node, snake_set):
    x, y = node
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < GRID and 0 <= ny < GRID:
            if (nx, ny) not in snake_set:
                yield (nx, ny)


def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def astar_path(start, goal, snake):
    snake_set = set(snake)
    open_list = []
    heapq.heappush(open_list, (0, start))
    came_from = {}
    g = {start: 0}

    while open_list:
        _, current = heapq.heappop(open_list)
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.reverse()
            return path

        for nb in neighbors(current, snake_set):
            tentative_g = g[current] + 1
            if tentative_g < g.get(nb, float("inf")):
                g[nb] = tentative_g
                f = tentative_g + heuristic(nb, goal)
                heapq.heappush(open_list, (f, nb))
                came_from[nb] = current
    return None


def ai_move():
    path = astar_path(snake[0], food, snake)
    if path and len(path) > 0:
        next_cell = path[0]
        dx = next_cell[0] - snake[0][0]
        dy = next_cell[1] - snake[0][1]
        return (dx, dy)
    else:
        # fallback: try safe moves
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = snake[0][0] + dx, snake[0][1] + dy
            if 0 <= nx < GRID and 0 <= ny < GRID and (nx, ny) not in snake:
                return (dx, dy)
    return direction


def step():
    global score
    head = (snake[0][0] + direction[0], snake[0][1] + direction[1])

    # Collisions
    if (
        head[0] < 0 or head[0] >= GRID or
        head[1] < 0 or head[1] >= GRID or
        head in snake
    ):
        reset()
        return

    snake.insert(0, head)

    if head == food:
        score += 1
        place_food()
    else:
        snake.pop()

    # If snake fills the grid, restart automatically
    if len(snake) >= GRID * GRID:
        reset()


# Initialize
reset()

# Main loop
running = True
speed = 10
while running:
    clock.tick(speed)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                ai_enabled = not ai_enabled
            elif not ai_enabled:
                if event.key in [pygame.K_UP, pygame.K_w] and direction != (0, 1):
                    direction = (0, -1)
                elif event.key in [pygame.K_DOWN, pygame.K_s] and direction != (0, -1):
                    direction = (0, 1)
                elif event.key in [pygame.K_LEFT, pygame.K_a] and direction != (1, 0):
                    direction = (-1, 0)
                elif event.key in [pygame.K_RIGHT, pygame.K_d] and direction != (-1, 0):
                    direction = (1, 0)

    if ai_enabled:
        direction = ai_move()

    step()
    draw()

pygame.quit()
