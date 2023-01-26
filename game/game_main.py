# coding=utf8

from game_class import *


pygame.mixer.pre_init(44100, -16, 2, 512)
mixer.init()  # ініціалізація модуля з музикою
pygame.init()  # ініціалізація модуля

clock = pygame.time.Clock()
fps = 60  # плавність

screen_width = 700  # розміри вікна ігрового
screen_height = 700

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("NAME OF GAME")  # назва

font = pygame.font.SysFont('COURNEUF REGULAR', 70)
font_score = pygame.font.SysFont('COURNEUF REGULAR', 30)  # шрифт

tile_size = 35  # розмір блоків
game_over = 0
main_menu = True
level = 1  # початковий рівень
max_levels = 7  # максимальна к-ть рівнів
score = 0  # рахунок

pink = (132, 89, 107)   # колір рахунку
blue = (220, 240, 247)  # колір написів
# фон
background_img = pygame.image.load('image/night_bg.jpg')

# кнопки
restart_img = pygame.image.load('image/restart.png')
restart_img = pygame.transform.scale(restart_img, (100, 40))
start_img = pygame.image.load('image/start.png')
start_img = pygame.transform.scale(start_img, (150, 70))
exit_img = pygame.image.load('image/exit.png')
exit_img = pygame.transform.scale(exit_img, (130, 50))

# музика
# pygame.mixer.music.load('back_m.wav')
# pygame.mixer.music.play(-1, 0.0, 5000)
coin_fx = pygame.mixer.Sound('sound/coin.wav')
coin_fx.set_volume(0.5)
jump_fx = pygame.mixer.Sound('sound/jump.wav')
jump_fx.set_volume(0.5)
game_over_fx = pygame.mixer.Sound('sound/game_over.wav')
game_over_fx.set_volume(0.5)

player = Player(65, screen_height - 100)  # де стоїть персоннаж на початку гри

blob_group = pygame.sprite.Group()  # відображення ворога
platform_group = pygame.sprite.Group()  # відображення платформ
lava_group = pygame.sprite.Group()  # відображення лави
star_group = pygame.sprite.Group()  # відображення зірок
exit_group = pygame.sprite.Group()  # перехід на інший рівень

score_star = Star(tile_size // 2, tile_size // 2)   # к-ть зірок
star_group.add(score_star)

# завантаження рівнів і створення світу
if path.exists(f'level{level}_data'):
    pickle_in = open(f'level{level}_data', 'rb')
    world_data = pickle.load(pickle_in)
world = World(world_data)  # відображення світу

# створення кнопок
restart_button = Button(screen_width // 2 - 50, screen_height // 2, restart_img)
start_button = Button(screen_width // 2 - 200, screen_height // 2, start_img)
exit_button = Button(screen_width // 2 + 80, screen_height // 1.96, exit_img)

run = True
while run:  # запуск гри
    clock.tick(fps)

    screen.blit(background_img, (0, 0))  # фон

    if main_menu is True:  # вивід головного меню
        if exit_button.draw():  # якщо ексіт - вихід з гри
            run = False
        if start_button.draw():  # якщо старт - початок гри
            main_menu = False

    else:
        world.draw()  # світ

        if game_over == 0:  # якщо гра йде - відображати
            blob_group.update()  # вороги
            platform_group.update()  # платформа
            if pygame.sprite.spritecollide(player, star_group, True):  # забирає зірки коли персонаж їх забрав
                score += 1
                coin_fx.play()  # музика збирання зірок
            draw_text(' x ' + str(score), font_score, pink, tile_size - 10, 10)

        blob_group.draw(screen)  # показ ворогів на екрані
        platform_group.draw(screen)  # показ платформ
        lava_group.draw(screen)  # для лави
        star_group.draw(screen)  # зірки
        exit_group.draw(screen)  # перехід

        game_over = player.update(game_over)  # персонаж програв

        if game_over == -1:  # якщо помирає - кнопка рестарт і все спочатку
            if restart_button.draw():
                world_data = []
                world = reset_level(level)
                game_over = 0
                score = 0

        if game_over == 1:  # перехід на інший рівень поки рівні не закінчаться
            level += 1
            if level <= max_levels:
                world_data = []
                world = reset_level(level)
                game_over = 0
            else:  # коли пройшов всі рівні - починає спочатку + текст перемоги
                draw_text('YOU WIN!', font, blue, (screen_width // 2) - 100, screen_height // 5)
                if restart_button.draw():
                    level = 1
                    world_data = []
                    world = reset_level(level)
                    game_over = 0
                    score = 0

                #  draw_grid()

    for event in pygame.event.get():  # вихід з гри
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()