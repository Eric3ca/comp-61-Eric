import pygame
import random

# Initialize
pygame.init()
pygame.mixer.init()  # Initialize the mixer module for sound

# Screen dimensions
WIDTH = 600
HEIGHT = 715
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird 2.0")

# Load assets
background = pygame.image.load(r"C:\Users\eric3\Desktop\comp61\download.png")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

bird_img = pygame.image.load(r"C:\Users\eric3\Desktop\comp61\bird.png")
bird = pygame.transform.scale(bird_img, (50, 50))

pipe_img = pygame.image.load(r"C:\Users\eric3\Desktop\comp61\342px-SMBW_Pipe.webp")
pipe_img = pygame.transform.scale(pipe_img, (80, 500))

plant_img = pygame.image.load(r"C:\Users\eric3\Desktop\comp61\584df4386a5ae41a83ddee0a.png")
plant_img = pygame.transform.scale(plant_img, (40, 40))

font = pygame.font.Font(r"C:\Users\eric3\Desktop\comp61\LEMONMILK-MediumItalic.otf", 32)

clock = pygame.time.Clock()

# Background Sound
pygame.mixer.music.load(r"C:\Users\eric3\Desktop\comp61\627052__victor_natas__dreams-made-of-mud-and-blood.wav")
pygame.mixer.music.play(-1)  # Play the background music in a loop

# Sounds
flap_sound = pygame.mixer.Sound(r"C:\Users\eric3\Desktop\comp61\123761__vicces1212__jump.wav")
hit_sound = pygame.mixer.Sound(r"C:\Users\eric3\Desktop\comp61\explosion.wav")

# Game variables
gravity = 0.5
bird_y = HEIGHT // 2
bird_vel = 0

pipe_gap = 150
pipe_x = WIDTH
pipe_height = random.randint(100, 400)

score = 0
high_score = 0
game_active = False
game_started = False

# Plant animation variables
plant_offset = 0
plant_direction = 1
plant_on_top = random.choice([True, False])  # Randomly choose plant position

def draw_pipe(x, height, offset, on_top):
    top_pipe = pygame.transform.flip(pipe_img, False, True)
    bottom_pipe = pipe_img

    # Draw pipes first
    screen.blit(top_pipe, (x, height - pipe_img.get_height()))
    screen.blit(bottom_pipe, (x, height + pipe_gap))

    # Draw plant (only one, based on random choice)
    if on_top:
        top_plant_img = pygame.transform.flip(plant_img, False, True)  # Flip plant vertically
        top_plant_y = height - top_plant_img.get_height() + offset
        screen.blit(top_plant_img, (x + 20, top_plant_y))
    else:
        bottom_plant_y = height + pipe_gap - offset
        screen.blit(plant_img, (x + 20, bottom_plant_y))

    # Redraw pipe edges over the plant to hide stems
    screen.blit(top_pipe, (x, height - pipe_img.get_height()))
    screen.blit(bottom_pipe, (x, height + pipe_gap))

def display_score(score, high_score):
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    high_text = font.render(f"High Score: {high_score}", True, (255, 215, 0))
    screen.blit(score_text, (10, 10))
    screen.blit(high_text, (10, 50))

def show_start_screen():
    title = font.render("Flappy Bird 2.0", True, (255, 215, 0))
    prompt = font.render("Press SPACE to Start", True, (255, 255, 255))
    screen.blit(title, (WIDTH // 2 - title.get_width() // 2, HEIGHT // 2 - 100))
    screen.blit(prompt, (WIDTH // 2 - prompt.get_width() // 2, HEIGHT // 2 - 30))

def show_game_over_screen():
    over_text = font.render("Game Over - Press SPACE", True, (255, 0, 0))
    screen.blit(over_text, (40, HEIGHT // 2 - 50))

# Game loop
running = True
while running:
    screen.blit(background, (0, 0))

    if not game_started:
        show_start_screen()
    elif game_active:
        # Bird movement
        bird_vel += gravity
        bird_y += bird_vel
        screen.blit(bird, (50, bird_y))

        # Pipe movement
        pipe_x -= 4
        if pipe_x < -80:
            pipe_x = WIDTH
            pipe_height = random.randint(100, 400)
            plant_on_top = random.choice([True, False])  # Randomize next pipe's plant
            score += 1

        # Animate plant offset
        plant_offset += plant_direction
        if plant_offset > 30 or plant_offset < 0:
            plant_direction *= -1

        draw_pipe(pipe_x, pipe_height, plant_offset, plant_on_top)

        # Collision detection
        bird_rect = pygame.Rect(50, bird_y, 50, 50)
        top_rect = pygame.Rect(pipe_x, pipe_height - pipe_img.get_height(), 80, pipe_img.get_height())
        bottom_rect = pygame.Rect(pipe_x, pipe_height + pipe_gap, 80, pipe_img.get_height())

        if plant_on_top:
            plant_rect = pygame.Rect(pipe_x + 20, pipe_height - plant_img.get_height() + plant_offset, 40, 40)
        else:
            plant_rect = pygame.Rect(pipe_x + 20, pipe_height + pipe_gap - plant_offset, 40, 40)

        if (bird_rect.colliderect(top_rect) or
                bird_rect.colliderect(bottom_rect) or
                bird_rect.colliderect(plant_rect) or
                bird_y > HEIGHT or bird_y < 0):
            hit_sound.play()
            game_active = False
            if score > high_score:
                high_score = score

        display_score(score, high_score)

    else:
        show_game_over_screen()
        display_score(score, high_score)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if not game_started:
                    game_started = True
                    game_active = True
                elif not game_active:
                    bird_y = HEIGHT // 2
                    bird_vel = 0
                    pipe_x = WIDTH
                    pipe_height = random.randint(100, 400)
                    score = 0
                    plant_offset = 0
                    plant_direction = 1
                    plant_on_top = random.choice([True, False])
                    game_active = True
                else:
                    bird_vel = -8
                    flap_sound.play()

    pygame.display.update()
    clock.tick(60)

pygame.quit()
