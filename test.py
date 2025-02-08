import GOL
import pygame
import sys

def sq_print(arr):
    n = len(arr)
    for i in range(n):
        print(arr[i])

pygame.init()

nbrs = [(1,0), (0,1), (-1,0), (0,-1), (1,1), (1,-1), (-1,1), (-1,-1)]
n = 20
m = 20
c = 2


colors = [ (255,255,255), (0,0,0)]

life = GOL.GOL(n, m, c, nbrs)
surface = pygame.display.set_mode((10*n, 10*m))

fd = open("world.txt", 'r')
count = 0
temp = [[0 for _ in range(m)] for _ in range(n)]
for line in fd:
    count += 1
    line = line.strip('\n')
    temp[count] = line.split(' ')

    for j in range(len(temp)):
        temp[count][j] = int(temp[count][j])
life.set_world(temp)




a = 0
a+= life.add_rule((1,(8,0)),0)
a+= life.add_rule((1,(7,1)),0)
a+= life.add_rule((1,(4,4)),0)
a+= life.add_rule((1,(3,5)),0)
a+= life.add_rule((1,(2,6)),0)
a+= life.add_rule((1,(1,7)),0)
a+= life.add_rule((1,(0,8)),0)

a+= life.add_rule((0,(5,3)),1)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            pygame.quit()
            sys.exit()

    for i in range(n):
        for j in range(m):
            color = colors[life.world[i][j]]
            pygame.draw.rect(surface, color, pygame.Rect(10*i,10*j,10,10))

    pygame.display.flip()
    life.update()
    pygame.time.wait(100)