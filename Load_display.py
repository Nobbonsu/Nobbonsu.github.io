import sys
import pygame
from pygame.locals import *

pygame.init()
pygame.display.set_caption('Optosol iDigital')
width = 1920
height = 1020

screen = pygame.display.set_mode((width, height), FULLSCREEN, vsync=1)
center_X, center_Y = screen.get_rect().centerx, screen.get_rect().centery
delta_Y = 0

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

running = True


def pause():
    global paused, delta_Y, fore_index, back_index, col_index, fore_col, back_col, size, index
    paused = True

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

        # screen.fill(0)
        pygame.display.update()


def num2():
    with open('load_text_2', 'r') as second:
        lines2 = second.read()

    global delta_Y, fore_index, back_index, col_index, fore_col, back_col, size, index
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
                elif event.key == pygame.K_RETURN:
                    pause()
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

            userInput2 = pygame.key.get_pressed()
            if userInput2[pygame.K_p]:
                pause()

        screen.fill(back_index)

        msg_list2 = []
        pos_list2 = []
        a1 = 0
        delta_Y -= 0.2

        font2 = pygame.font.SysFont('Arial', size, bold=True, italic=False)
        # msg = font.render(lines, True, fore_index, back_index)

        for line2 in lines2.split('\n'):
            msg2 = font2.render(line2, True, fore_index, back_index)
            msg_list2.append(msg2)
            pos2 = msg2.get_rect(center=(center_X, center_Y + delta_Y + a1 * 150))
            pos_list2.append(pos2)
            a1 = a1 + 1

        if center_Y + delta_Y + 80 * (len(lines2.split('\n'))) < 0:
            delta_Y = 250

        for b in range(a1):
            screen.blit(msg_list2[b], pos_list2[b])

        pygame.display.update()


def num():
    with open('load_text_1', 'r') as first:
        lines1 = first.read()

    global delta_Y, fore_index, back_index, col_index, fore_col, back_col, size, index
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
                elif event.key == pygame.K_RETURN:
                    pause()
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

            userInput1 = pygame.key.get_pressed()
            if userInput1[pygame.K_p]:
                pause()

        screen.fill(back_index)

        msg_list1 = []
        pos_list1 = []
        a = 0
        delta_Y -= 0.2

        font1 = pygame.font.SysFont('Arial', size, bold=True, italic=False)
        # msg = font.render(lines, True, fore_index, back_index)

        for line1 in lines1.split('\n'):
            msg1 = font1.render(line1, True, fore_index, back_index)
            msg_list1.append(msg1)
            pos1 = msg1.get_rect(center=(center_X, center_Y + delta_Y + a * 130))
            pos_list1.append(pos1)
            a = a + 1

        if center_Y + delta_Y + 80 * (len(lines1.split('\n'))) < 0:
            delta_Y = 250

        for b in range(a):
            screen.blit(msg_list1[b], pos_list1[b])

        pygame.display.update()


def welcome():
    while running:
        screen.fill(black)
        text = """
        Welcome to Optosol iRead
        Press Space Bar To Start Reading
        Escape Key To Exit"""

        text_list = []
        position_list = []
        i = 0

        font = pygame.font.SysFont('comicsansms', 100, bold=True, italic=False)

        for texts in text.split('\n'):
            screen_text = font.render(texts, True, yellow, black)
            text_list.append(screen_text)
            position = screen_text.get_rect(center=(center_X-200, center_Y-300 + i*150))
            position_list.append(position)
            i = i + 1

        for j in range(i):
            screen.blit(text_list[j], position_list[j])

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


def mainLoop():
    with open('load_text', 'r') as main:
        words = main.read()

    global delta_Y, fore_index, back_index, col_index, fore_col, back_col, index, size, paused

    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()
                # running = False
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    welcome()
                    # running = False
                elif event.key == pygame.K_RETURN:
                    pause()
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

            # userInput = pygame.key.get_pressed()
            # if userInput[pygame.K_p]:
            #     pause()

        screen.fill(back_index)

        msg_list = []
        pos_list = []
        i = 0
        delta_Y -= 0.2

        font = pygame.font.SysFont('Arial', size, bold=True, italic=False)
        # msg = font.render(lines, True, fore_index, back_index)

        for line in words.split('\n'):
            msg = font.render(line, True, fore_index, back_index)
            msg_list.append(msg)
            pos = msg.get_rect(center=(center_X, center_Y + delta_Y + i * 100))
            pos_list.append(pos)
            i = i + 1

        if center_Y + delta_Y + 80 * (len(words.split('\n'))) < 0:
            delta_Y = 250

        for j in range(i):
            screen.blit(msg_list[j], pos_list[j])

        pygame.display.update()


welcome()
pygame.quit()
