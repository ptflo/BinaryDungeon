# Example file showing a circle moving on screen
import pygame, sys, tkinter
from tkinter import Button

# pygame setup
pygame.init()
SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Binary Dungeon")
BACKGROUND = pygame.image.load("Resources/backgrounds/main_menu.jpg")


def get_font(size: int):
    return pygame.font.Font("Resources/fonts/pixelify.ttf", size)

def play():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")

        PLAY_TEXT = get_font(45).render("This is the PLAY screen.", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Button(image=None, pos=(640, 460),
                           text="BACK", font=get_font(75), highlightcolor="Green")

        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        OPTIONS_TEXT = get_font(45).render("This is the OPTIONS screen.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(640, 460),
                              text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def main_menu():
    pygame.display.set_caption("Binary Dungeon")
    while True:
        SCREEN.blit(BACKGROUND, (0, 0))
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        MENU_TEXT = get_font(100).render("HLAVNÍ NABÍDKA", True, "#D7B498")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))
        pb = tkinter.PhotoImage(file="Resources/buttons/play.png")
        label = tkinter.Label(image=pb)
        label.pack()
        label.pb = pb

        PLAY_BUTTON = Button(image=label.pb, font=get_font(75), text="HRÁT", highlightcolor="#efd39b")
        # OPTIONS_BUTTON = Button(image=pygame.image.load("Resources/buttons/options.png"), font=get_font(75), text="NASTAVENÍ",
        #                      highlightcolor="#efd39b")
        # QUIT_BUTTON = Button(image=pygame.image.load("Resources/buttons/quit.png"), font=get_font(75), text="ODEJÍT",
        #                      highlightcolor="#efd39b")
        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()
# clock = pygame.time.Clock()
# running = True
# dt = 0
#
# screen_middle = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
#
# while running:
#     # poll for events
#     # pygame.QUIT event means the user clicked X to close your window
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#
#     # fill the screen with a color to wipe away anything from last frame
#     screen.fill("purple")
#
#     pygame.draw.circle(screen, "red", screen_middle, 40)
#
#     keys = pygame.key.get_pressed()
#     if keys[pygame.K_w]:
#         screen_middle.y -= 300 * dt
#     if keys[pygame.K_s]:
#         screen_middle.y += 300 * dt
#     if keys[pygame.K_a]:
#         screen_middle.x -= 300 * dt
#     if keys[pygame.K_d]:
#         screen_middle.x += 300 * dt
#
#     # flip() the display to put your work on screen
#     pygame.display.flip()
#
#     # limits FPS to 60
#     # dt is delta time in seconds since last frame, used for framerate-
#     # independent physics.
#     dt = clock.tick(60) / 1000
#
# pygame.quit()
