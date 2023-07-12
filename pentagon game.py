import pygame

import math





weight, high = 400, 400

line_weight = 50

black = 0, 0, 0

white = 255, 255, 255

brown = 139, 105, 20

peachpuff = 255, 218, 185

Turquoise1 = 0, 245, 255

chess = []

chess_coordinate = []

direction = "N"

match_x, match_y = -1, -1







def search_match(screen):

    global direction

    global match_x

    global match_y

    count = 0

    click_x, click_y = int(chess[len(chess)-1][1]/line_weight), int(chess[len(chess)-1][0]/line_weight)

    tag = chess_coordinate[click_x][click_y]

    print(click_x,click_y)



    #水平方向

    for i in range(0,5):

        if click_y + i < len(chess_coordinate) and click_y + i - 4 >= 0:

            x, y = click_x, click_y+i

            while y >= click_y - 4:

                if tag == chess_coordinate[x][y]:

                    count += 1

                    y -= 1

                else:

                    count = 0

                    break

                if count == 5:

                    count = 0

                    print("L", click_x, click_y + i)

                    direction, match_x, match_y = "L", click_x, click_y + i



                    #return "L", click_x, click_y + i



    #竖直方向

    for i in range(0,5):

        if click_x + i < len(chess_coordinate) and click_x + i - 4 >= 0:

            x, y = click_x + i, click_y

            while x >= click_x - 4:

                if tag == chess_coordinate[x][y]:

                    count += 1

                    x -= 1

                else:

                    count = 0

                    break

                if count == 5:

                    count = 0

                    print("U", click_x + i, click_y)

                    direction, match_x, match_y = "U", click_x + i, click_y

                    #return "U", click_x + i, click_y



    #主对角

    for i in range(0,5):

        if click_x + i < len(chess_coordinate) and click_x + i - 4 >= 0 and click_y + i < len(chess_coordinate) and click_y + i - 4 >= 0:

            x, y = click_x + i, click_y + i

            while x >= click_x - 4 and y >= click_y - 4:

                if tag == chess_coordinate[x][y]:

                    count += 1

                    x -= 1

                    y -= 1

                else:

                    count = 0

                    break

                if count == 5:

                    count = 0

                    print("LU", click_x + i, click_y + i)

                    direction, match_x, match_y = "LU", click_x + i, click_y + i

                    #return "LU", click_x + i, click_y + i



    #副对角

    for i in range(0,5):

        if click_x + i < len(chess_coordinate) and click_x + i - 4 >= 0 and click_y - i >= 0 and click_y - i + 4 >= 0:

            x, y = click_x + i, click_y - i

            while x >= click_x - 4 and y <= click_y + 4:

                if tag == chess_coordinate[x][y]:

                    count += 1

                    x -= 1

                    y += 1

                else:

                    count = 0

                    break

                if count == 5:

                    count = 0

                    print("RU", click_x + i, click_y - i)

                    direction, match_x, match_y = "RU", click_x + i, click_y - i

                    #return "RU", click_x + i, click_y - i





def set_chess_corrdinate():

    for i in range(int(weight/line_weight)+1):

        chess_coordinate.append([])

        for j in range(int(high/line_weight)+1):

            chess_coordinate[i].append(0)





def print_chess_coordinate():

    for i in range(int(weight / line_weight)+1):

        for j in range(int(high / line_weight)+1):

            print(chess_coordinate[i][j], end=" ")

        print()





def draw_chessboard(screen):

    x, y = 0, 0

    for i in range(int(high/line_weight)):

        x = i * line_weight

        y = i * line_weight

        pygame.draw.aaline(screen, black, [x, 0], [x, high], True)

        pygame.draw.aaline(screen, black, [0, y], [weight, y], True)





def search_chess(Mouse_x, Mouse_y, turn):

    left_up_x = int(Mouse_x / line_weight) * line_weight

    left_up_y = int(Mouse_y / line_weight) * line_weight



    four_possible_node = [[left_up_x, left_up_y], [left_up_x + line_weight, left_up_y], [left_up_x, left_up_y + line_weight], [left_up_x + line_weight, left_up_y + line_weight]]



    i = 0

    min = 0

    Node = 0

    for node in four_possible_node:

        d = math.pow((Mouse_x - node[0]), 2) + math.pow((Mouse_y - node[1]), 2)

        if i == 0:

            min = d

            Node = i

        else:

            if d < min:

                min = d

                Node = i

        i += 1

    if four_possible_node[Node] not in chess:

        chess.append(four_possible_node[Node])

        if turn % 2 == 0:

            chess_coordinate[int(four_possible_node[Node][1]/line_weight)][int(four_possible_node[Node][0]/line_weight)] = 1

        else:

            chess_coordinate[int(four_possible_node[Node][1] / line_weight)][

                int(four_possible_node[Node][0] / line_weight)] = -1

        #return int(four_possible_node[Node][0]/line_weight), int(four_possible_node[Node][1]/line_weight)





def draw_chess(screen, chess, direction, match_x, match_y):



    for node in chess:

        if chess.index(node) % 2 == 0:

            pygame.draw.circle(screen, black, (node[0], node[1]), int(line_weight/3), 0)

        else:

            pygame.draw.circle(screen, white, (node[0], node[1]), int(line_weight/3), 0)



    if direction == "L":

        for i in range(5):

            pygame.draw.circle(screen, Turquoise1, ((match_y - i) * int(line_weight), (match_x) * int(line_weight)), int(line_weight/3), 0)

    elif direction == "U":

        for i in range(5):

            pygame.draw.circle(screen, Turquoise1, ((match_y) * int(line_weight), (match_x - i) * int(line_weight)),

                               int(line_weight / 3), 0)

    elif direction == "LU":

        for i in range(5):

            pygame.draw.circle(screen, Turquoise1, ((match_y - i) * int(line_weight), (match_x - i) * int(line_weight)),

                               int(line_weight / 3), 0)

    elif direction == "RU":

        for i in range(5):

            pygame.draw.circle(screen, Turquoise1, ((match_y + i) * int(line_weight), (match_x - i) * int(line_weight)),

                               int(line_weight / 3), 0)





if __name__ == "__main__":

    pygame.init()

    screen = pygame.display.set_mode((weight, high))

    pygame.display.set_caption("五子棋")

    white = 255, 255, 255

    Mouse_x, Mouse_y = -100, -100

    turn = 0

    set_chess_corrdinate()







    while True:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                exit()

            if event.type == pygame.MOUSEBUTTONDOWN and direction == "N":

                Mouse_x, Mouse_y = event.pos

                turn += 1

                search_chess(Mouse_x, Mouse_y, turn)

                print_chess_coordinate()

                search_match(screen)





        screen.fill(brown)

        draw_chessboard(screen)

        draw_chess(screen, chess, direction, match_x, match_y)





        pygame.display.update()

