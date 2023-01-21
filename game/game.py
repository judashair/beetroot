import pygame
from pygame.locals import *
import pickle
from os import path

pygame.init() # ініціалізація модуля

clock = pygame.time.Clock()
fps = 60 # плавність

screen_width = 700 # розміри вікна ігрового
screen_height = 700

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("NAME OF GAME") # назва

tile_size = 35 # розмір блоків
game_over = 0
main_menu = True
level = 0 # початковий рівень
max_levels = 7 # максимальна к-ть рівнів
# фон
background_img = pygame.image.load('night_bg.jpg')

# кнопки
restart_img = pygame.image.load('restart.png')
restart_img = pygame.transform.scale(restart_img, (100, 40))
start_img = pygame.image.load('start.png')
start_img = pygame.transform.scale(start_img, (150, 70))
exit_img = pygame.image.load('exit.png')
exit_img = pygame.transform.scale(exit_img, (130, 50))


#функція для скидання рівня
def reset_level(level):
    player.reset(65, screen_height - 100)
    # очищує все
    blob_group.empty()
    lava_group.empty()
    exit_group.empty()

    # завантаження рівнів і створення світу
    if path.exists(f'level{level}_data'):
        pickle_in = open(f'level{level}_data', 'rb')
        world_data = pickle.load(pickle_in)
    world = World(world_data)  # відображення світу

    return world

# def draw_grid():  #  розмітка для кращого будвання блоків
#     for line in range(0, 20):
#         pygame.draw.line(screen, (255, 255, 255), (0, line * tile_size), (screen_width, line * tile_size))
#         pygame.draw.line(screen, (255, 255, 255), (line * tile_size, 0), (line * tile_size, screen_height))
# для кнопок старту/рестарту
class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.clicked = False

    # показ кнопок ігрових
    def draw(self):
        action = False

        # де курсор
        pos = pygame.mouse.get_pos()

        # перевірка чи курсор на кнопці і клікнув
        if self.rect.collidepoint(pos): # чи курсор на кнопці
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked is False: # якщо клікнуто лівою (0) кнопкою миші
                action = True
                self.clicked = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        screen.blit(self.image, self.rect)

        return action


class Player(): # опис персонажа
    def __init__(self, x, y):
        self.reset(x, y)

    def update(self, game_over):
        dx = 0
        dy = 0
        walk_cooldown = 8

        if game_over == 0:  # поки не програв
            # керування
            key = pygame.key.get_pressed()
            if key[pygame.K_SPACE] and self.jumped is False and self.in_air is False:
                self.vel_y = -15
                self.jumped = True
            if key[pygame.K_SPACE] is False:
                self.jumped = False
            if key[pygame.K_LEFT]:
                dx -= 5
                self.counter += 1
                self.direction = -1
            if key[pygame.K_RIGHT]:
                dx += 5
                self.counter += 1
                self.direction = 1
            if key[pygame.K_LEFT] is False and key[pygame.K_RIGHT] is False:
                self.counter = 0
                self.index = 0
                if self.direction == 1: # щоб розвертався в тому напрямку куди нажимається стрілка
                    self.image = self.images_right[self.index]
                if self.direction == -1:
                    self.image = self.images_left[self.index]

            # animation
            if self.counter > walk_cooldown:
                self.counter = 0
                self.index += 1
                if self.index >= len(self.images_right):
                    self.index = 0
                if self.direction == 1:
                    self.image = self.images_right[self.index]
                if self.direction == -1:
                    self.image = self.images_left[self.index]

            # гравітація
            self.vel_y += 1
            if self.vel_y > 10:
                self.vel_y = 10
            dy += self.vel_y

            # колізія
            self.in_air = True
            for tile in world.tile_list:
                # x direction collision
                if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                    dx = 0

                # y direction collision
                if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                    # перевірка чи над землею - прижок
                    if self.vel_y < 0:
                        dy = tile[1].bottom - self.rect.top
                        self.vel_y = 0
                    # падіння
                    elif self.vel_y >= 0:
                        dy = tile[1].top - self.rect.bottom
                        self.vel_y = 0
                        self.in_air = False # прижок тільки один раз

            # колізія з енемі
            if pygame.sprite.spritecollide(self, blob_group, False):  #якщо натрапив на ворогів - програш
                game_over = -1

            # колізія з лавою
            if pygame.sprite.spritecollide(self, lava_group, False):  # те саме для лави
                game_over = -1

            if pygame.sprite.spritecollide(self, exit_group, False): # якщо доходить до виходу - наступний рівень
                game_over = 1

            self.rect.x += dx
            self.rect.y += dy

        elif game_over == -1:  # якщо програш - зображення привида
            self.image = self.dead_image
            self.image = pygame.transform.scale(self.image, (tile_size, tile_size))
            if self.rect.y > 200:
                self.rect.y -= 5

        screen.blit(self.image, self.rect)
        pygame.draw.rect(screen, (255, 255, 255), self.rect, 2)

        return game_over

    def reset(self, x, y):
        self.images_right = []
        self.images_left = []
        self.index = 0
        self.counter = 0
        for num in range(1, 5):
            img_right = pygame.image.load(f'gg{num}.png')
            img_right = pygame.transform.scale(img_right, (32, 60)) # зменшення фото
            img_left = pygame.transform.flip(img_right, True, False)  # відзеркалює зображання вертикально в даному випадку
            self.images_right.append(img_right)
            self.images_left.append(img_left)
            # опис його положення
        self.dead_image = pygame.image.load('dead.png')
        self.image = self.images_right[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.vel_y = 0
        self.jumped = False
        self.direction = 0
        self.in_air = True


class World(): # опис світу
    def __init__(self, data):
        self.tile_list = []

        cake_img = pygame.image.load('cake.png')
        cream_img = pygame.image.load('cream.png')

        row_count = 0
        for row in data:
            col_count = 0
            for tile in row:
                if tile == 1: # яке зображення брати якщо в матриці стоїть 1
                    img = pygame.transform.scale(cake_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 2: # для 2
                    img = pygame.transform.scale(cream_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 3: # для 3 - ворог
                    blob = Enemy(col_count * tile_size, row_count * tile_size + 5)
                    blob_group.add(blob)
                if tile == 6:  # лава
                    lava = Lava(col_count * tile_size, row_count * tile_size + (tile_size // 2))
                    lava_group.add(lava)
                if tile == 8: # вихід
                    exit = Exit(col_count * tile_size, row_count * tile_size - (tile_size // 2))
                    exit_group.add(exit)
                col_count += 1
            row_count += 1

    def draw(self):
        for tile in self.tile_list:
            screen.blit(tile[0], tile[1])
            pygame.draw.rect(screen, (255, 255, 255), tile[1], 2)


class Enemy(pygame.sprite.Sprite): # опис ворога
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('enemy.png')
        self.image = pygame.transform.scale(self.image, (30, 30)) # зменшення зображення
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move_direction = 1 # рух
        self.move_counter = 0

    def update(self):
        self.rect.x += self.move_direction
        self.move_counter += 1
        if self.move_counter > 40: # щоб не виходили за межі блоків
            self.move_direction *= -1
            self.move_counter *= -1


class Lava(pygame.sprite.Sprite):  # для лави
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('lava.png')
        self.image = pygame.transform.scale(img, (tile_size, tile_size // 2)) # зменшення зображення
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Exit(pygame.sprite.Sprite):  # для переходу на інший рівень
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('door.png')
        self.image = pygame.transform.scale(img, (tile_size, int(tile_size * 1.5))) # зменшення зображення
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


# мапа світу
# world_data = [
#     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#     [1, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 1],
#     [1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 2, 2, 1],
#     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 7, 0, 5, 0, 0, 0, 1],
#     [1, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 1],
#     [1, 7, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#     [1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 7, 0, 0, 0, 0, 1],
#     [1, 0, 2, 0, 0, 7, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#     [1, 0, 0, 2, 0, 0, 4, 0, 0, 0, 0, 3, 0, 0, 3, 0, 0, 0, 0, 1],
#     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 0, 0, 0, 1],
#     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 7, 0, 0, 0, 0, 2, 0, 1],
#     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 2, 0, 2, 2, 2, 2, 2, 1],
#     [1, 0, 0, 0, 0, 0, 2, 2, 2, 6, 6, 6, 6, 6, 1, 1, 1, 1, 1, 1],
#     [1, 0, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#     [1, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#     [1, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# ]

player = Player(65, screen_height - 100) # де стоїть персоннаж на початку гри

blob_group = pygame.sprite.Group() # відображення ворога
lava_group = pygame.sprite.Group()  # відображення лави
exit_group = pygame.sprite.Group() # перехід на інший рівень

# завантаження рівнів і створення світу
if path.exists(f'level{level}_data'):
    pickle_in = open(f'level{level}_data', 'rb')
    world_data = pickle.load(pickle_in)
world = World(world_data) # відображення світу

# створення кнопок
restart_button = Button(screen_width // 2 - 50, screen_height // 2, restart_img)
start_button = Button(screen_width // 2 - 200, screen_height // 2, start_img)
exit_button = Button(screen_width // 2 + 80, screen_height // 1.96, exit_img)

run = True
while run: # запуск гри
    clock.tick(fps)

    screen.blit(background_img, (0, 0)) # фон

    if main_menu is True: # вивід головного меню
        if exit_button.draw(): # якщо ексіт - вихід з гри
            run = False
        if start_button.draw(): # якщо старт - початок гри
            main_menu = False

    else:
        world.draw() # світ

        if game_over == 0:  # якщо гра йде - відображати
            blob_group.update() # вороги

        blob_group.draw(screen)  # показ ворогів на екрані
        lava_group.draw(screen)  # для лави
        exit_group.draw(screen) #  перехід

        game_over = player.update(game_over) # персонаж програв

        if game_over == -1: # якщо помирає - кнопка рестарт
            if restart_button.draw():
                world_data = []
                world = reset_level(level)
                game_over = 0

        if game_over == 1: # переід на інший рівень поки рівні не закінчаться
            level += 1
            if level <= max_levels:
                world_data = []
                world = reset_level(level)
                game_over = 0
            else: # коли пройшов всі рівні - починає спочатку
                if restart_button.draw():
                    level = 1
                    world_data = []
                    world = reset_level(level)
                    game_over = 0


                # draw_grid()

    for event in pygame.event.get(): # вихід з гри
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
