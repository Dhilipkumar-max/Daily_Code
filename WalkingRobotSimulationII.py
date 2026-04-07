class Robot(object):

    def __init__(self, width, height):
        self.w = width
        self.h = height
        self.pos = 0
        self.perimeter = 2 * (width + height - 2)
        self.moved = False

    def step(self, num):
        self.moved = True
        self.pos = (self.pos + num) % self.perimeter

    def getPos(self):
        curr = self.pos
        if 0 <= curr <= self.w - 1:
            return [curr, 0]
        elif self.w <= curr <= self.w + self.h - 2:
            return [self.w - 1, curr - (self.w - 1)]
        elif self.w + self.h - 1 <= curr <= 2 * self.w + self.h - 3:
            return [self.w - 1 - (curr - (self.w + self.h - 2)), self.h - 1]
        else:
            return [0, self.perimeter - curr]

    def getDir(self):
       
        if self.moved and self.pos == 0:
            return "South"
        
        curr = self.pos
        if 1 <= curr <= self.w - 1:
            return "East"
        elif self.w <= curr <= self.w + self.h - 2:
            return "North"
        elif self.w + self.h - 1 <= curr <= 2 * self.w + self.h - 3:
            return "West"
        else:
            return "South" if self.moved else "East"
