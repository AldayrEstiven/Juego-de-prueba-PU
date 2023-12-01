pip install pygame
import pygame
import random

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Esquivar Obstáculos")

# Colores
white = (255, 255, 255)
black = (0, 0, 0)

# Jugador
player_size = 50
player_x = width // 2 - player_size // 2
player_y = height - 2 * player_size
player_speed = 5

# Obstáculos
obstacle_size = 50
obstacle_speed = 5
obstacle_frequency = 25
obstacles = []

# Reloj para controlar la velocidad de actualización
clock = pygame.time.Clock()

# Puntuación
score = 0
font = pygame.font.SysFont(None, 30)

# Función para mostrar la puntuación en la pantalla
def show_score(score):
    score_text = font.render("Puntuación: " + str(score), True, white)
    screen.blit(score_text, (10, 10))

# Bucle principal del juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    player_x += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * player_speed

    # Generar obstáculos
    if random.randrange(0, obstacle_frequency) == 0:
        obstacle_x = random.randrange(0, width - obstacle_size)
        obstacle_y = -obstacle_size
        obstacles.append([obstacle_x, obstacle_y])

    # Mover y dibujar obstáculos
    for obstacle in obstacles:
        obstacle[1] += obstacle_speed
        pygame.draw.rect(screen, white, (obstacle[0], obstacle[1], obstacle_size, obstacle_size))

        # Verificar colisión con el jugador
        if (
            player_x < obstacle[0] < player_x + player_size
            or player_x < obstacle[0] + obstacle_size < player_x + player_size
        ) and (
            player_y < obstacle[1] < player_y + player_size
            or player_y < obstacle[1] + obstacle_size < player_y + player_size
        ):
            running = False

    # Eliminar obstáculos que han salido de la pantalla
    obstacles = [obstacle for obstacle in obstacles if obstacle[1] < height]

    # Dibujar jugador
    pygame.draw.rect(screen, white, (player_x, player_y, player_size, player_size))

    # Actualizar puntuación
    score += 1

    # Mostrar puntuación en la pantalla
    show_score(score)

    # Actualizar la pantalla
    pygame.display.update()

    # Establecer la velocidad de actualización
    clock.tick(30)

# Salir del juego
pygame.quit()