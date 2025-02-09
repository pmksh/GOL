import GOL
import pygame
import sys

def sq_print(arr):
    n = len(arr)
    for i in range(n):
        print(arr[i])

pygame.init()

nbrs = [(1,0), (0,1), (-1,0), (0,-1)]
n = 40
m = 40
c = 3


colors = [ (200,0,0), (150,0,0), (100,0,0)]

life = GOL.GOL(n, m, c, nbrs)
surface = pygame.display.set_mode((10*n, 10*m))

fd = open("world3.txt", 'r')
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
a+= life.add_rule((0,(0,1,3)),1)
a+= life.add_rule((0,(1,1,2)),1)
a+= life.add_rule((0,(2,1,1)),1)
a+= life.add_rule((0,(3,1,0)),1)
a+= life.add_rule((0,(0,2,2)),1)
a+= life.add_rule((0,(1,2,1)),1)
a+= life.add_rule((0,(2,2,0)),1)
a+= life.add_rule((0,(1,3,0)),1)
a+= life.add_rule((0,(0,3,1)),1)
a+= life.add_rule((0,(0,4,0)),1)


a+= life.add_rule((1,(0,3,1)),2)
a+= life.add_rule((1,(1,2,1)),2)
a+= life.add_rule((1,(2,1,1)),2)
a+= life.add_rule((1,(3,0,1)),2)
a+= life.add_rule((1,(0,2,2)),2)
a+= life.add_rule((1,(1,1,2)),2)
a+= life.add_rule((1,(2,0,2)),2)
a+= life.add_rule((1,(1,0,3)),2)
a+= life.add_rule((1,(0,1,3)),2)
a+= life.add_rule((1,(0,0,4)),2)


a+= life.add_rule((2,(1,0,3)),0)
a+= life.add_rule((2,(1,1,2)),0)
a+= life.add_rule((2,(1,2,1)),0)
a+= life.add_rule((2,(1,3,0)),0)
a+= life.add_rule((2,(2,0,2)),0)
a+= life.add_rule((2,(2,1,1)),0)
a+= life.add_rule((2,(2,2,0)),0)
a+= life.add_rule((2,(3,1,0)),0)
a+= life.add_rule((2,(3,0,1)),0)
a+= life.add_rule((2,(4,0,0)),0)


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