import sys
import pygame
from pygame.locals import *
from pygame import mixer

import TextLoad

pygame.init()
pygame.display.set_caption('Optosol iDigital')
width = 1920
height = 1020

mixer.init()

screen = pygame.display.set_mode((width, height), FULLSCREEN, vsync=1)
center_X, center_Y = screen.get_rect().centerx, screen.get_rect().centery
delta_Y = 0
delta = [0.2, 0.4, 0.6, 0.8, 1, 1.2, 1.4, 1.6, 1.8, 2]
delta_index = 0
delta_num = delta[delta_index]

white = (255, 255, 255)
black = (0, 0, 0)
yellow = (255, 255, 0)
fore_col = [(0, 0, 0), (255, 255, 255), (255, 255, 255), (0, 0, 255), (0, 0, 0), (255, 255, 0)]
back_col = [(255, 255, 255), (0, 0, 0), (0, 0, 255), (255, 255, 255), (255, 255, 0), (0, 0, 0)]
col_index = 0
fore_index = fore_col[col_index]
back_index = back_col[col_index]

text_size = [60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180]
index = 0
size = text_size[index]


def playText():
    mixer.music.load('Temp_Audio/test.mp3')
    mixer.music.play()


def welcomeText():
    mixer.music.load('Temp_Audio/welcome.mp3')
    mixer.music.play()


def pausePlay():
    mixer.music.pause()


def unpausePlay():
    mixer.music.unpause()


def stopPlay():
    mixer.music.stop()


def increaseSpeed():
    global delta, delta_num, delta_index
    if delta_index == 9:
        delta_index = 0
    else:
        delta_index += 1
    delta_num = delta[delta_index]


def decreaseSpeed():
    global delta, delta_num, delta_index
    if delta_index >= 1:
        delta_index -= 1
    delta_num = delta[delta_index]


read_img = pygame.image.load('icon/conductor-icon.png').convert_alpha()


class Button:
    def __init__(self, x, y, image, scale):
        width_1 = image.get_width()
        height_1 = image.get_height()
        self.image = pygame.transform.scale(image, (int(width_1 * scale), int(height_1 * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self):
        action = False
        # get mouse position
        pos = pygame.mouse.get_pos()

        # check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        screen.blit(self.image, (self.rect.x, self.rect.y))

        return action


read_button = Button(1800, 950, read_img, 0.5)

with TextLoad.CustomOpen('string.txt') as f:
    lines = f.read()
    original_stdout = sys.stdout
    with TextLoad.CustomWrite('new_text') as file:
        for key, val in enumerate(lines.split(), start=1):
            sys.stdout = file
            if key % 4 == 0:
                print(val, end='\n\n')
            else:
                print(val, end=' ')
            sys.stdout = original_stdout

with TextLoad.CustomOpen('string.txt') as f:
    lines1 = f.read()
    original_stdout = sys.stdout
    with TextLoad.CustomWrite('new_text_1') as file:
        for key, val in enumerate(lines1.split(), start=1):
            sys.stdout = file
            if key % 3 == 0:
                print(val, end='\n\n')
            else:
                print(val, end=' ')
            sys.stdout = original_stdout

with TextLoad.CustomOpen('string.txt') as f:
    lines = f.read()
    original_stdout = sys.stdout
    with TextLoad.CustomWrite('new_text_2') as file:
        for key, val in enumerate(lines.split(), start=1):
            sys.stdout = file
            if key % 2 == 0:
                print(val, end='\n\n')
            else:
                print(val, end=' ')
            sys.stdout = original_stdout


def pause():
    global paused, delta_Y, fore_index, back_index, col_index, fore_col, back_col, size, index

    paused = True

    pausePlay()

    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    paused = False
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()

        # screen.fill(0)
        pygame.display.update()


def num2():
    with open('new_text_2', 'r') as second:
        lines2 = second.read()

    global delta_Y, fore_index, back_index, col_index, fore_col, back_col, size, index, paused, delta_num, delta_index, delta
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    welcome()
                elif event.key == pygame.K_RETURN:
                    pause()
                    unpausePlay()
                elif event.key == pygame.K_SPACE:
                    if col_index == 5:
                        col_index = 0
                    else:
                        col_index += 1
                    fore_index = fore_col[col_index]
                    back_index = back_col[col_index]
                elif event.key == pygame.K_RIGHT:
                    mainLoop()
                elif event.key == pygame.K_LEFT:
                    num()
                elif event.key == pygame.K_b:
                    if col_index > 0:
                        col_index -= 1
                    fore_index = fore_col[col_index]
                    back_index = back_col[col_index]
                elif event.key == pygame.K_UP:
                    if index == 12:
                        index = 0
                    else:
                        index += 1
                    size = text_size[index]
                elif event.key == pygame.K_DOWN:
                    if index <= 12:
                        index -= 1
                    size = text_size[index]
                elif event.key == pygame.K_z:
                    increaseSpeed()
                elif event.key == pygame.K_x:
                    decreaseSpeed()
                elif event.key == pygame.K_p:
                    playText()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    increaseSpeed()
                elif event.button == 3:
                    decreaseSpeed()

        screen.fill(back_index)

        if read_button.draw():
            playText()

        msg_list2 = []
        pos_list2 = []
        a1 = 0
        delta_Y -= delta_num

        font2 = pygame.font.SysFont('Arial', size, bold=True, italic=False)
        # msg = font.render(lines, True, fore_index, back_index)

        for line2 in lines2.split('\n'):
            msg2 = font2.render(line2, True, fore_index, back_index)
            msg_list2.append(msg2)
            pos2 = msg2.get_rect(center=(center_X, center_Y + delta_Y + a1 * 150))
            pos_list2.append(pos2)
            a1 = a1 + 1

        if center_Y + delta_Y + 100 * (len(lines2.split('\n'))) < 0:
            delta_Y = 300

        for b in range(a1):
            screen.blit(msg_list2[b], pos_list2[b])

        pygame.display.update()


def num():
    with open('new_text_1', 'r') as first:
        lines2 = first.read()

    global delta_Y, fore_index, back_index, col_index, fore_col, back_col, size, index, delta_num, delta_index, delta, paused
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    welcome()
                elif event.key == pygame.K_RETURN:
                    pause()
                    unpausePlay()
                elif event.key == pygame.K_SPACE:
                    if col_index == 5:
                        col_index = 0
                    else:
                        col_index += 1
                    fore_index = fore_col[col_index]
                    back_index = back_col[col_index]
                elif event.key == pygame.K_RIGHT:
                    num2()
                elif event.key == pygame.K_LEFT:
                    mainLoop()
                elif event.key == pygame.K_b:
                    if col_index > 0:
                        col_index -= 1
                    fore_index = fore_col[col_index]
                    back_index = back_col[col_index]
                elif event.key == pygame.K_UP:
                    if index == 10:
                        index = 0
                    else:
                        index += 1
                    size = text_size[index]
                elif event.key == pygame.K_DOWN:
                    if index <= 12:
                        index -= 1
                    size = text_size[index]
                elif event.key == pygame.K_z:
                    increaseSpeed()
                elif event.key == pygame.K_x:
                    decreaseSpeed()
                elif event.key == pygame.K_p:
                    playText()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    increaseSpeed()
                elif event.button == 3:
                    decreaseSpeed()

        screen.fill(back_index)

        if read_button.draw():
            playText()

        msg_list1 = []
        pos_list1 = []
        a = 0
        delta_Y -= delta_num

        font1 = pygame.font.SysFont('Arial', size, bold=True, italic=False)
        # msg = font.render(lines, True, fore_index, back_index)

        for line1 in lines2.split('\n'):
            msg1 = font1.render(line1, True, fore_index, back_index)
            msg_list1.append(msg1)
            pos1 = msg1.get_rect(center=(center_X, center_Y + delta_Y + a * 130))
            pos_list1.append(pos1)
            a = a + 1

        if center_Y + delta_Y + 100 * (len(lines2.split('\n'))) < 0:
            delta_Y = 300

        for b in range(a):
            screen.blit(msg_list1[b], pos_list1[b])

        pygame.display.update()


def welcome():
    stopPlay()

    running = True
    while running:
        screen.fill(back_index)
        text = """
        Welcome to Optosol iRead
        Press Space Bar To Start Reading
        Escape Key To Exit"""

        text_list = []
        position_list = []
        i = 0

        font = pygame.font.SysFont('comicsansms', 100, bold=True, italic=False)

        for texts in text.split('\n'):
            screen_text = font.render(texts, True, fore_index, back_index)
            text_list.append(screen_text)
            position = screen_text.get_rect(center=(center_X - 200, center_Y - 300 + i * 150))
            position_list.append(position)
            i = i + 1

        for j in range(i):
            screen.blit(text_list[j], position_list[j])

        if read_button.draw():
            welcomeText()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_SPACE:
                    mainLoop()
        pygame.display.update()
        # clock.tick(60)


def mainLoop():
    with open('new_text', 'r') as mainRead:
        words = mainRead.read()

    global delta_Y, fore_index, back_index, col_index, fore_col, back_col, index, size, paused, delta_num, delta_index, delta
    running = True
    reading_complete = False
    while running:
        if reading_complete:
            screen.fill(back_index)
            text = 'Press Enter To Read Again'
            font = pygame.font.SysFont('comicsansms', 80, bold=True, italic=False)
            complete_text = font.render(text, True, fore_index, back_index)
            screen.blit(complete_text, (center_X, center_Y))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    if event.key == pygame.K_y:
                        welcome()
                        pygame.display.update()
        else:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        welcome()
                    elif event.key == pygame.K_RETURN:
                        pause()
                        unpausePlay()
                    elif event.key == pygame.K_SPACE:
                        if col_index == 5:
                            col_index = 0
                        else:
                            col_index += 1
                        fore_index = fore_col[col_index]
                        back_index = back_col[col_index]

                    elif event.key == pygame.K_RIGHT:
                        num()
                    elif event.key == pygame.K_b:
                        if col_index > 0:
                            col_index -= 1
                        fore_index = fore_col[col_index]
                        back_index = back_col[col_index]
                    elif event.key == pygame.K_UP:
                        if index == 6:
                            index = 0
                        else:
                            index += 1
                        size = text_size[index]
                    elif event.key == pygame.K_DOWN:
                        if index <= 12:
                            index -= 1
                        size = text_size[index]
                    elif event.key == pygame.K_z:
                        increaseSpeed()
                    elif event.key == pygame.K_x:
                        decreaseSpeed()
                    elif event.key == pygame.K_p:
                        playText()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        increaseSpeed()
                    elif event.button == 3:
                        decreaseSpeed()

        screen.fill(back_index)

        if read_button.draw():
            try:
                playText()
            except NameError as e:
                print(e)

        msg_list = []
        pos_list = []
        i = 0
        # delta_Y -= 0.2
        delta_Y -= delta_num

        font = pygame.font.SysFont('Arial', size, bold=True, italic=False)
        # msg = font.render(lines, True, fore_index, back_index)

        for line in words.split('\n'):
            msg = font.render(line, True, fore_index, back_index)
            msg_list.append(msg)
            pos = msg.get_rect(center=(center_X, center_Y + delta_Y + i * 100))
            pos_list.append(pos)
            i = i + 1

        if center_Y + delta_Y + 100 * (len(words.split('\n'))) < 0:
            delta_Y = 300

        for j in range(i):
            screen.blit(msg_list[j], pos_list[j])

        pygame.display.update()


def main():
    welcome()
    pygame.quit()


if __name__ == "__main__":
    main()
