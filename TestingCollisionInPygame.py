import pygame
import sys
class Ball:
    def __init__(self,x,y,r):
        self.x = x
        self.y = y
        self.r = r
        self.sx = 1
        self.sy = 1
    def Draw(self):
        pygame.draw.circle(screen,(0,0,0),(self.x,self.y),self.r)
    def Move(self):
        self.y += self.sy
        self.x += self.sx
        #self.sy += 0.1635
        if self.y+self.r >500:
            self.y -= (self.y+self.r - 500)
            self.sy = -self.sy
        if self.y-self.r < 0:
            self.y += (self.y+self.r)
            self.sy = -self.sy
        if self.x-self.r < 0:
            self.x += (self.x+self.r)
            self.sx = -self.sx
        if self.x+self.r > 500:
            self.x -= (self.x+self.r - 500)
            self.sx = -self.sx
        
        
pygame.init()
screen = pygame.display.set_mode((500, 500))
screen.fill((255,255,255))
pygame.display.flip()
clock = pygame.time.Clock()
Object = Ball(100,100,10)
running = True
held = False
Previous = [0,0]
while running:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            running = False
    screen.fill((255,255,255))
    Object.Draw()
    Object.Move()
    if  pygame.mouse.get_pressed()[0]:
        if pygame.mouse.get_pos()[0] > (Object.x-Object.r) and pygame.mouse.get_pos()[0] < (Object.x+Object.r):
            if pygame.mouse.get_pos()[1] > (Object.y-Object.r) and pygame.mouse.get_pos()[1] < (Object.y+Object.r):
                held = True
    else:
        if held:
            Object.sx = -round((Previous[0] -Object.x))
            Object.sy = -round((Previous[1] -Object.y))
        held = False
    if held:
        Previous = [Object.x,Object.y]
        Object.x = pygame.mouse.get_pos()[0]
        Object.y = pygame.mouse.get_pos()[1]
                
    clock.tick(30)
