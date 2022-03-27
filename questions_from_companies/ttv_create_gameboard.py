"""
Write an algorithm which populates an MxN board
with exactly X enemies
Assume that X does not exceed the number of spaces available.

1, 1, 0, 0, 1
0, 1, 1, 0, 0
1, 0, 0, 0, 1
0, 1, 1, 0, 0
1, 1, 0, 1, 0
"""
import random


def getRandXY(width, height):
    x = random.randint(0, width-1)
    y = random.randint(0, height-1)
    return x,y


def create_gameboard1(width, height, numEnemies):
    matrix = [[0 for x in range(width)] for y in range(height)]
    for i in range(0, numEnemies):
        x, y = getRandXY(width, height)
        # during the interview we discussed that this was the area most likely
        # to have performance issues, the while loop with the collisions
        while matrix[x][y] == 1:
            print('collision')
            x, y = getRandXY(width, height)
        matrix[x][y] = 1
    print(matrix)
    return matrix


# alternative solution post-interview:
# use a dict to keep track of enemy positions
# looking up enemy position in dict faster than looking up a big matrix
def create_enemy_map(width, height, numEnemies):
    enemy_map = {}
    for i in range(numEnemies):
        pos = (getRandXY(width, height))
        while pos in enemy_map:
            pos = (getRandXY(width, height))
        enemy_map[pos] = 1
    print(enemy_map)
    return enemy_map


def create_gameboard(width, height, numEnemies):
    matrix = [[0 for x in range(width)] for y in range(height)]
    enemy_map = create_enemy_map(width, height, numEnemies)
    for location in enemy_map.keys():
        x, y = location
        matrix[x][y] = 1
    print(matrix)
    return matrix


create_gameboard(5, 5, 7)
