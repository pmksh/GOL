import random

class GOL:

    def __init__(self, n, m, colors, nbrs):
        self.n = n
        self.m = m
        self.c = colors #from 0 to colors-1
        self.nbrs = nbrs
        self.ln = len(nbrs)
        # nbr is a set of (x,y) where (x,y) is the relative address of neighbor
        # if (0,0) or duplicates, may make weird results


        self.world = [[0 for _ in range(m)] for _ in range(n)]

        self.rules = {}
        # rule format (a,(x_0,...,x_{c-1})) : b
        # a is current state color
        # b is the transitioned color
        # x_i is the number of color i squares in neighborhood
        # ln = x_0 + ... +x_{c-1}

    def set_world(self, world):
        n = len(world)
        m = len(world[0])
        if n!=self.n or m!= self.m:
            return -1
        self.world = world
        return 1
    
    def set_world_random(self):
        for i in range(self.n):
            for j in range(self.m):
                self.world[i][j] = random.randint(0,self.c-1)

    def set_state(self, x, y, color):
        if x >= self.n or y >= self.m or color >= self.c:
            return -1
        self.world[x][y] = color
        return 1

    def add_rule(self, cond, trans):

        if trans >= self.c or cond[0] >= self.c:
            return -1
        if len(cond[1]) != self.c:
            return -1
        sum = 0
        for i in range(self.c):
            sum += cond[1][i]

        if sum != self.ln:
            return -1

        self.rules[cond] = trans
        return 1

    def update(self):
        new_world = [[0 for _ in range(self.m)] for _ in range(self.n)]

        for i in range(self.n):
            for j in range(self.m):
                count = [0 for _ in range(self.c)]

                for nbr in self.nbrs:
                    x = nbr[0] % self.n
                    y = nbr[1] % self.m

                    count[self.world[(i+x) % self.n][(j+y) % self.m]] += 1

                count = tuple(count)
                cond = (self.world[i][j], count)
                if cond in self.rules:
                    new_world[i][j] = self.rules[cond]
                else:
                    new_world[i][j] = self.world[i][j]

        self.world = new_world


