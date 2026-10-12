import math
import random
import pygame

screen_width, screen_height = 800, 500
Player_Start_x, Player_Start_y = 370, 380
Enemy_Start_Y_MIN= 50
Enemy_Start_Y_MAX= 150
Enemy_Speed_X= 4
Enemy_Speed_Y= 40
Bullet_Speed= 10
Collision_Distance= 27

pygame.init()
screen= pygame.display.set_mode((screen_width, screen_height))

background = pygame.image.load("bg.jpg")

pygame.display.set_caption("Space Invaders")
icon= pygame.image.load("Ufo.png")
pygame.display.set_icon(icon)

playerImg = pygame.transform.scale(

pygame.image.load('Spaceship.png'),

(80, 80) # width, height

)
PlayerX= Player_Start_x
PlayerY= Player_Start_y
PlayerX_change= 0

EnemyImg= []
EnemyX= []
EnemyY= []
EnemyX_change= []
EnemyY_change= []
num_of_enemies= 6

for i in range(num_of_enemies):
    EnemyImg.append(

    pygame.transform.scale())
    EnemyX.append(random.randint(0, screen_width - 64))
    EnemyY.append(random.randint(Enemy_Start_Y_MIN, Enemy_Start_Y_MAX))
    EnemyX_change.append(Enemy_Speed_X)
    EnemyY_change.append(Enemy_Speed_Y)

bulletImg = pygame.transform.scale(pygame.image.load('bullet.png'),(20, 40))
bulletX= 0
bulletY= Player_Start_y
bulletX_change= 0
bulletY_change= Bullet_Speed
bullet_state= "ready"

score_value= 0
font= pygame.font.Font("freesansbold.ttf", 32)
textX= 10
textY= 10

over_font= pygame.font.Font("freesansbold.ttf", 64)

def show_score(x, y):
    score= font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def game_over_text():
    over_text= over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))

def player(x, y):
    screen.blit(playerImg, (x,y))

def enemy(x, y, i):
    screen.blit(EnemyImg[i], (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance= math.sqrt((enemyX - bulletX) ** 2 + (enemyY - bulletY) ** 2)
    return distance < Collision_Distance


running= True

while running:
    screen.fill((0,0,0))
    screen.blit(background , (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                PlayerX_change = -5
            if event.key == pygame.K_RIGHT:
                PlayerX_change = 5
            if event.key == pygame.K_SPACE and bullet_state == "ready":
                bulletX = PlayerX
                fire_bullet(bulletX, bulletY)
            if event.type == pygame.KEYUP and event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                PlayerX_change = 0

    PlayerX += PlayerX_change
    playerX = max(0, min(PlayerX, screen_width - 64))

    for i in range (num_of_enemies):
        if EnemyY[i] > 340:
            for j in range(num_of_enemies):
                EnemyY[j] = 2000
            game_over_text()
            break

        EnemyX[i] += EnemyX_change[i]
        if EnemyX[i] <= 0 or EnemyX[i] >= screen_width - 64:
            EnemyX_change[i] *= -1
            EnemyY[i] += EnemyY_change[i]

        if isCollision(EnemyX[i], EnemyY[i], bulletX, bulletY):
            bulletY = Player_Start_y
            bullet_state = "ready"
            score_value += 1
            EnemyX[i] = random.randint(0, screen_width - 64)
            EnemyY[i] = random.randint(Enemy_Start_Y_MIN, Enemy_Start_Y_MAX)

        enemy(EnemyX[i], EnemyY[i], i)

        if bulletY <= 0:
            bulletY = Player_Start_y
            bullet_state = "ready"

        elif bullet_state == "fire":
            fire_bullet(bulletX, bulletY)
            bulletY -= bulletY_change

        player(PlayerX, PlayerY)
        show_score(textX, textY)
        pygame.display.update()