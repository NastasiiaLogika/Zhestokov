import pygame
import sys

# Ініціалізація Pygame
pygame.init()

# Встановлення розмірів екрану
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Clicker Game")

# Кольори
WHITE = (255, 255, 255)
BLUE = (135, 206, 235)
LIGHT_BLUE = (173, 216, 230)

# Шрифти
font = pygame.font.Font(None, 48)
small_font = pygame.font.Font(None, 24)

# Змінні гри
counter = 0
click_value = 1
auto_click_value = 0
auto_clickers = 0
multiplier = 1
prestige_points = 0

# Функція для відображення тексту на екрані
def draw_text(text, font, color, rect):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=rect.center)
    screen.blit(text_surface, text_rect)

# Основний цикл гри
running = True
while running:
    screen.fill(BLUE)

    # Обробка подій
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Ліва кнопка миші
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if click_button_rect.collidepoint(mouse_x, mouse_y):
                    counter += click_value * multiplier
                elif upgrade_click_button_rect.collidepoint(mouse_x, mouse_y) and counter >= click_value * 10:
                    counter -= click_value * 10
                    click_value += 1
                elif auto_clicker_button_rect.collidepoint(mouse_x, mouse_y) and counter >= (auto_clickers + 1) * 50:
                    counter -= (auto_clickers + 1) * 50
                    auto_clickers += 1
                    auto_click_value = auto_clickers
                elif multiplier_button_rect.collidepoint(mouse_x, mouse_y) and counter >= multiplier * 100:
                    counter -= multiplier * 100
                    multiplier += 1
                    click_value = click_value*2
                elif prestige_button_rect.collidepoint(mouse_x, mouse_y) and counter >= 1000:
                    counter = 0
                    click_value = 1
                    auto_clickers = 0
                    auto_click_value = 0
                    multiplier = 1
                    prestige_points += 1
                elif super_clicker_button_rect.collidepoint(mouse_x, mouse_y) and counter >= 500:
                    counter -= 500
                    click_value += 10
                elif mega_multiplier_button_rect.collidepoint(mouse_x, mouse_y) and counter >= 2000:
                    counter -= 2000
                    multiplier += 5

    # Малювання кнопок
    click_button_rect = pygame.draw.rect(screen, LIGHT_BLUE, (150, 200, 200, 100))
    upgrade_click_button_rect = pygame.draw.rect(screen, LIGHT_BLUE, (400, 50, 200, 50))
    auto_clicker_button_rect = pygame.draw.rect(screen, LIGHT_BLUE, (400, 150, 200, 50))
    multiplier_button_rect = pygame.draw.rect(screen, LIGHT_BLUE, (400, 250, 200, 50))
    prestige_button_rect = pygame.draw.rect(screen, LIGHT_BLUE, (400, 350, 200, 50))
    super_clicker_button_rect = pygame.draw.rect(screen, LIGHT_BLUE, (150, 350, 200, 50))
    mega_multiplier_button_rect = pygame.draw.rect(screen, LIGHT_BLUE, (150, 450, 200, 50))

    # Малювання тексту на кнопках
    draw_text(f"Click {click_value}", font, WHITE, click_button_rect)
    draw_text(f"Upgrade Click ({click_value * 10})", small_font, WHITE, upgrade_click_button_rect)
    draw_text(f"Auto-Clicker ({(auto_clickers + 1) * 50})", small_font, WHITE, auto_clicker_button_rect)
    draw_text(f"Multiplier ({multiplier * 100})", small_font, WHITE, multiplier_button_rect)
    draw_text(f"Prestige (1000 Clicks)", small_font, WHITE, prestige_button_rect)
    draw_text(f"Super Clicker (500)", small_font, WHITE, super_clicker_button_rect)
    draw_text(f"Mega Multiplier (2000)", small_font, WHITE, mega_multiplier_button_rect)

    # Відображення лічильника над кнопкою
    draw_text(f"{counter}", font, WHITE, pygame.Rect(150, 100, 200, 100))

    # Оновлення екрану
    pygame.display.flip()

# Вихід з Pygame
pygame.quit()
sys.exit()