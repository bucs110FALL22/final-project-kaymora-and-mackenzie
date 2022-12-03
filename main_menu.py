import pygame
import sys
from controller import Button
from dropdown import DropDown
import json

pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Dine Before you Try!")

#BG = pygame.image.load('assets/background.png')
BG = pygame.image.load('assets/background.png')


def get_font(size):
    return pygame.font.Font("assets/font.ttf", size)

r = open('restaurant.json', 'r')
restaurants = json.load(r)

def makeRest(loc, restNum):
    if restNum == 1:
        posX = 180
    elif restNum == 2:
        posX = 640
    else:
        posX = 1100

    Res_image = pygame.image.load(f'assets/{restaurants[loc][f"Rest{restNum}"]["images"]}')

    name_surf = get_font(15).render(restaurants[loc][f"Rest{restNum}"]["name"], True, 'Black')
    name_rect = name_surf.get_rect(center=(posX, 100))

    addy_surf = get_font(10).render(restaurants[loc][f"Rest{restNum}"]["address"], True, 'Black')
    addy_rect = addy_surf.get_rect(center=(posX, 180))

    num_surf = get_font(15).render(restaurants[loc][f"Rest{restNum}"]["phoneNumber"], True, 'Black')
    num_rect = num_surf.get_rect(center=(posX, 260))

    img_surf = pygame.transform.scale(Res_image,(80,80))
    img_rect = img_surf.get_rect(center=(posX, 340))

    price_surf = get_font(15).render(f'${restaurants[loc][f"Rest{restNum}"]["price"]}', True, 'Black')
    price_rect = price_surf.get_rect(center=(posX, 430))

    SCREEN.blit(name_surf, name_rect)
    SCREEN.blit(addy_surf, addy_rect)
    SCREEN.blit(num_surf, num_rect)
    SCREEN.blit(img_surf,img_rect)
    SCREEN.blit(price_surf,price_rect)


class Controller():

    def __init__(self):
        self.clock = pygame.time.Clock()

    def start(self):
        START_TEXT = get_font(25).render("Where do you live?", True, "White")
        START_RECT = START_TEXT.get_rect(center=(640, 80))

        COLOR_INACTIVE = (100, 80, 255)
        COLOR_ACTIVE = (100, 200, 255)
        COLOR_LIST_INACTIVE = (255, 100, 100)
        COLOR_LIST_ACTIVE = (255, 150, 150)

        START_BACK = Button(image=None,
                            pos=(640, 460),
                            text_input="BACK",
                            font=get_font(75),
                            base_color="white",
                            hovering_color="pink")

        list1 = DropDown([COLOR_INACTIVE, COLOR_ACTIVE],
                         [COLOR_LIST_INACTIVE, COLOR_LIST_ACTIVE], 540, 150, 200,
                         50, pygame.font.SysFont(None,
                                                 30), "Where do you live?",
                         ["New York City", "Seattle", "Atlanta"])

        while True:
            SCREEN.fill("light blue")
            START_MOUSE_POS = pygame.mouse.get_pos()

            event_list = pygame.event.get()

            for event in event_list:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if START_BACK.check(START_MOUSE_POS):
                        self.main_menu()
                    if list1.check_drop() and list1.check(list1.buttons[0], START_MOUSE_POS):
                        self.restaurant("New York City")
                    if list1.check_drop() and list1.check(list1.buttons[1], START_MOUSE_POS):
                        self.restaurant("Seattle")
                    if list1.check_drop() and list1.check(list1.buttons[2], START_MOUSE_POS):
                        self.restaurant("Atlanta")
            t = list1.update(event_list)
            if type(t) == tuple():
                print(t)

            SCREEN.blit(START_TEXT, START_RECT.topleft)
            START_BACK.hover(START_MOUSE_POS)
            START_BACK.on_screen(SCREEN)

            list1.draw(SCREEN)

            pygame.display.update()

    def main_menu(self):
        while True:
            SCREEN.blit(BG, (0, 0))

            MENU_MOUSE_POS = pygame.mouse.get_pos()

            MENU_TEXT = get_font(55).render("DINE BEFORE YOU TRY!", True,
                                            "#add8e6")

            MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

            START_BUTTON = Button(image=None,
                                  pos=(640, 400),
                                  text_input="START",
                                  font=get_font(75),
                                  base_color="white",
                                  hovering_color="pink")

            QUIT_BUTTON = Button(image=None,
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
                        self.start()
                    if QUIT_BUTTON.check(MENU_MOUSE_POS):
                        pygame.quit()
                        sys.exit()

            pygame.display.update()

    def restaurant(self, loc):

        Restaurant_BACK = Button(image=None,
                                pos=(640, 650),
                                text_input="BACK",
                                font=get_font(35),
                                base_color="Black",
                                hovering_color="pink")



        while True:
            SCREEN.fill("coral")
            Restaurant_Mouse_Pos = pygame.mouse.get_pos()
            Restaurant_TEXT = get_font(25).render(f"{loc} Restaurants!",
                                                 True, "black")
            Restaurant_RECT = Restaurant_TEXT.get_rect(center=(640, 40))

            # name_surf = get_font(10).render("Restaurant Name", True, 'Black')
            # name_rect = name_surf.get_rect(center=(120, 100))
            #
            # addy_surf = get_font(10).render("Res addy", True, 'Black')
            # addy_rect = addy_surf.get_rect(center=(120, 120))

            makeRest(loc, 1)
            makeRest(loc, 2)
            makeRest(loc, 3)

            SCREEN.blit(Restaurant_TEXT, Restaurant_RECT)

            Restaurant_BACK.hover(Restaurant_Mouse_Pos)
            Restaurant_BACK.on_screen(SCREEN)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if Restaurant_BACK.check(Restaurant_Mouse_Pos):
                        self.start()

            pygame.display.update()


run = Controller()
run.main_menu()
