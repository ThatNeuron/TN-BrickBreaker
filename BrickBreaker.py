import pygame
from paddle import Paddle
from ball import Ball
from brick import Brick

# Initialize Pygame
pygame.init()

# Configure the display
WIDTH = 800
HEIGHT = 700
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Brick Breaker')

score = 0
lives = 3

# Set the colors
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (50,100,200)
GRAY = (220,220,220)

# Configure the clock
FPS = 60
clock = pygame.time.Clock()

# Instantiate the paddle
paddle = Paddle()
paddle.rect.x = (WIDTH/2) - 60
paddle.rect.y = HEIGHT - 60

# Instantiate the ball
ball = Ball()
ball.initialPos()

# Group of sprites
allSprites = pygame.sprite.Group()
allSprites.add(paddle)
allSprites.add(ball)

# Group of bricks
allBricks = pygame.sprite.Group()

#Instantiate Bricks
def instBricks(c,r):
    for i in range(c):
        for j in range(r):
            brick = Brick(BLUE)
            brick.rect.x = 20 + i*110
            brick.rect.y = 20 + j*30
            allBricks.add(brick)
            allSprites.add(brick)

instBricks(7,9)

def removeBricks():
    for brick in allBricks:
        brick.kill()

# Adding the sound effect
brickSound = pygame.mixer.Sound('C:/Users/KONICRIUM/OneDrive/Documents/Workspace/MyPythonProjects/PythonGames/BrickBreaker/Sound/Brick.wav')
lostSound = pygame.mixer.Sound('C:/Users/KONICRIUM/OneDrive/Documents/Workspace/MyPythonProjects/PythonGames/BrickBreaker/Sound/Downer01.wav')

#Main Loop
start = False
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen
    screen.fill(GRAY)

    # Draw the sprites
    allSprites.draw(screen)

    # Handle Key events
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        start = True
    if keys[pygame.K_RIGHT]:
        paddle.moveRight()
    if keys[pygame.K_LEFT]:
        paddle.moveLeft()

    # Score
    font = pygame.font.Font(None, 40)
    text = font.render(f'Score: {score}', 1, BLACK)
    screen.blit(text, (20, HEIGHT-30))
    # Lives
    font = pygame.font.Font(None, 40)
    text = font.render(f'Lives: {lives}', 1, BLACK)
    screen.blit(text, (WIDTH-120, HEIGHT-30))

    if lives == 0:
        font = pygame.font.Font(None, 40)
        text = font.render(f'GAME OVER', 1, BLACK)
        screen.blit(text, (300, 350))
        font = pygame.font.Font(None, 40)
        text = font.render(f'PRESS SPACE TO PLAY', 1, BLACK)
        screen.blit(text, (250, 450))
    if len(allBricks)== 0:
        font = pygame.font.Font(None, 40)
        text = font.render(f'YOU WON', 1, BLACK)
        screen.blit(text, (300, 350))
        ball.initialPos()
        start = False

    if start :
        #Update the Sprites
        allSprites.update()
        if lives == 0:
            lives = 3
            score = 0
            removeBricks()
            instBricks(7,9)
        if ball.rect.right >= WIDTH or ball.rect.left <= 0:
            ball.bounceX()
        if ball.rect.top <= 0:
            ball.bounceY()
        if ball.rect.y >= HEIGHT - 40:
            lostSound.play()
            ball.initialPos()
            lives -= 1
            start = False

        # Collision with the paddle
        if ball.rect.colliderect(paddle.rect):
            if abs(paddle.rect.top - ball.rect.bottom) < 9:
                ball.bounceY()
            if abs(paddle.rect.left - ball.rect.right) < 9 or abs(paddle.rect.right - ball.rect.left) < 9:
                ball.bounceX()
        # Collision with the bricks
        ballHitList = pygame.sprite.spritecollide(ball,allBricks,False)
        for brick in ballHitList:
            brickSound.play()
            ball.bounceY()
            brick.kill()
            score += 1

    # Draw a line
    pygame.draw.line(screen, BLACK,[0,HEIGHT-35], [WIDTH,HEIGHT-35], 5)

    # Update the display
    pygame.display.update()

    # Tick the clock
    clock.tick(FPS)

# Close the game
pygame.quit()