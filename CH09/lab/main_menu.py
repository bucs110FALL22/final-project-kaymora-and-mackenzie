import pygame, sys
from controller import Button

pygame.init()

SCREEN = pygame.display.set_mode((1280,720))
pygame.display.set_caption("Dine Before you Try!")

#BG = pygame.image.load('assets/background.png')
BG = pygame.image.load('background.png')


def get_font(size):
    return pygame.font.Font("assets/font.ttf", size)


def start():

    while True:
        START_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("light blue")
        START_TEXT = get_font(45).render("Where do you live?", True, "White")
        START_RECT = START_TEXT.get_rect(center=(1,1))
        SCREEN.blit(START_TEXT, START_RECT)

        START_BACK = Button(image=None, pos=(640, 460), text_input="BACK", 
        font=get_font(75),base_color="white",hovering_color="pink")

        START_BACK.hover(START_MOUSE_POS)
        START_BACK.on_screen(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if START_BACK.check(START_MOUSE_POS):
                    main_menu()

            pygame.display.update()


def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))
        button_surface = pygame.image.load('assets/button.png')
        button_surface = pygame.transform.scale(button_surface,(200,150))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("DINE BEFORE YOU TRY!", True,
                                         "#add8e6")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        START_BUTTON = Button(button_surface,
                              pos=(640, 250),
                              text_input="START",
                              font=get_font(75),
                              base_color="black",
                              hovering_color="pink")

        QUIT_BUTTON = Button(image=pygame.image.load('assets/button_quit.png'),
                             pos=(640, 550),
                             text_input="QUIT",
                             font=get_font(75),
                             base_color="white",
                             hovering_color="pink")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [START_BUTTON, QUIT_BUTTON]:
            button.hover(MENU_MOUSE_POS)
            button.on_screen(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if START_BUTTON.check(MENU_MOUSE_POS):
                    start()
                if QUIT_BUTTON.check(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


main_menu()
