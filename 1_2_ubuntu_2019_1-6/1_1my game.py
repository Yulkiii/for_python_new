import pygame
from random import randint
from math import sqrt
from enum import Enum,unique

def main():
    
    balls=[]
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Big eat small')

    screen.fill((255, 255, 255))
    pygame.display.flip()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
           x,y=event.pos
           radius=randint(10,100)
           sx,sy=randint(-10,10),randint(-10,10)
           color=Color.random_color()
           ball=Ball(x,y,radius,sx,sy,color)
           balls.append(ball)
        screen.fill((255, 255, 255))
        for ball in balls:
            assert isinstance(ball.alive, object)
            if ball.alive:
                ball.draw(screen)
            else:
                balls.remove(ball)

        pygame.display.flip()
        pygame.time.delay(30)
        for ball in balls:
            ball.move(screen)
            for others in balls:
                ball.eat(others)
            if ball.radius>=250:
                balls=[]
                
@unique                
class Color(Enum):
    RED=(225,0,0)
    GREEN=(0,225,0)
    BLUE=(0,0,225)
    WHITE=(225,225,225)
    BLACK=(0,0,0)
    @staticmethod
    def random_color():
        r=randint(0,255)
        g=randint(0,255)
        b=randint(0,255)
        return(r,g,b)
class Ball(object):
    def __init__(self,x,y,radius,sx,sy,color=Color.RED):
        self.x=x
        self.y=y
        self.radius=radius
        self.sx=sx
        self.sy=sy
        self.color=color
        self.alive=True

    def move(self,screen):
        self.x+=self.sx
        self.y+=self.sy
        if self.x-self.radius<=0 or \
           self.x+self.radius>=screen.get_width():
            self.sx=-self.sx
        if self.y-self.radius<=0 or \
           self.y+self.radius>=screen.get_height():
            self.sy=-self.sy

    def eat(self,other):
        if self.alive and other.alive and self != other:
            dx, dy = self.x - other.x, self.y - other.y
            distance = sqrt(dx ** 2 + dy ** 2)
            if distance < self.radius + other.radius \
                    and self.radius > other.radius:
                other.alive = False
                self.radius = self.radius + int(other.radius * 0.146)

    def draw(self,screen):
        pygame.draw.circle(screen,self.color,(self.x,self.y),self.radius,0)

        
            

if __name__=='__main__':
    main()
