import random
import pygame
import sys

# Pygame init
pygame.init()

# Window
WIDTH, HEIGHT = 1200, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Card Battle")

# Background
background = pygame.image.load("background.png")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0,255,0)

# Class enemies
class EnemyCard:
    def __init__(self, name, strength, image_path, hp):
        self.name = name
        self.strength = strength
        self.hp = hp  # HP for enemies
        self.max_hp = hp
        self.image = pygame.image.load(image_path)
        self.heal_count = 0  # Healing counter for enemies

# Ennemies
enemies = [
    EnemyCard("The (Metal) Slug", 10, "Slug.png", 50),
    EnemyCard("The Rogue (don't trust him)", 15, "Rogue.png", 75),
    EnemyCard("The Necromancer", 20, "Necromancer.png", 100),
]

# Player (Hero)
player_hp = 100
player_max_hp = 100
player_turn = True  # Turn by turn

# Player's card (Always the same)
player_image = pygame.image.load("Hero.png")

# def for text
def draw_text(text, font, color, x, y):
    text_obj = font.render(text, True, color)
    screen.blit(text_obj, (x, y))

# Main loop
running = True
enemy = random.choice(enemies)  # Choose a random enemy
font = pygame.font.SysFont(None, 40)

while running:
    # backscreen
    screen.blit(background, (0, 0))

    # Display player and ennemy
    draw_text(f"HP Hero {player_hp}/{player_max_hp}", font, BLUE, 20, 20)
    draw_text(f"HP Ennemy: {enemy.name} - HP: {enemy.hp}/{enemy.max_hp} - Force: {enemy.strength}", font, RED, 20, 80)

    # Display Ennemy's card
    screen.blit(enemy.image, (WIDTH - enemy.image.get_width() - 20, 20))

    # Display Palyer's card
    screen.blit(player_image, (20, HEIGHT - player_image.get_height() - 20))

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Commands
        if player_turn and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:  # 1 for Attack
                enemy_damage = random.randint(5, 15)
                enemy.hp = max(enemy.hp - enemy_damage, 0)
                print(f"You strike the ennemy {enemy_damage} points of damage !")
                player_turn = False  # Ennemy' turn
            elif event.key == pygame.K_2:  # 2 for Magic
                print("You use magic !")
                player_turn = False  # Ennemy' turn
            elif event.key == pygame.K_3:  # 3 for item
                player_hp = min(player_hp + 20, player_max_hp)
                print("You recover a part of your HP with a potion!")
                player_turn = False  # Ennemy' turn

    # Ennemy's turn
    if not player_turn:
        if enemy.hp <= enemy.max_hp * 0.3 and enemy.heal_count < 2:  # 2 by turn Max
            # Enemy chose to healing
            heal_amount = random.choice([5, 10, 20])
            enemy.hp = min(enemy.hp + heal_amount, enemy.max_hp)
            enemy.heal_count += 1  # Increase heal count
            print(f"The enemy heals and recover {heal_amount} HP !")
        else:
            # Enemy attack the player
            player_damage = random.randint(5, 15)
            player_hp = max(player_hp - player_damage, 0)
            print(f"The enemy attack the Hero {player_damage} damage !")

        # Player's turn
        player_turn = True

    # Endgame conditions
    if player_hp <= 0:
        print("You have fallen after a tragic battle!")
        running = False
    elif enemy.hp <= 0:
        print("You kill the Enemy, congratulation !")
        running = False

    # Player's options
    if player_turn:
        draw_text("1 for Attack", font, GREEN, WIDTH - 500, 450)
        draw_text("2 for Magic", font, GREEN, WIDTH - 500, 500)
        draw_text("3 for Items", font, GREEN, WIDTH - 500, 550)

    # Update the display
    pygame.display.flip()

pygame.quit()
