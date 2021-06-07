import pygame,time
from math import atan, pi, sin, cos, tan
from pygame import draw
class ant:
    def __init__(self):
        self.dircetion = 270
        self.pos = [300,300]
        self.r = 1
        self.sensor_corners = [1,1,0,0]
        self.sensor_size = 50
        self.sensor_colour = (255,0,0)
    def draw_sensor(self,win):
        pygame.draw.circle(win,self.sensor_colour,self.pos,self.sensor_size,self.sensor_size,self.sensor_corners[0],self.sensor_corners[1],
        self.sensor_corners[2],self.sensor_corners[3])
        return
    def change_angle(self,value,win):
        self.dircetion+=value
        if self.dircetion in range(0,91):
            self.sensor_corners = [1,1,1,0]
        elif self.dircetion in range(91,181):
            self.sensor_corners = [0,1,1,1]
        elif self.dircetion in range(181,271):
            self.sensor_corners = [1,0,1,1]
        else:
            self.sensor_corners = [1,1,0,1]
        self.draw_sensor(win)
        return
    def move_to_food(self,food):
        x_change = food[0]-self.pos[0]
        y_change = self.pos[1]-food[1]
        print(x_change,y_change)
        angle = atan(x_change/y_change)
        angle = angle*180/pi
        if y_change<0:
            angle+=360
            if x_change<0:
                angle-=180
        elif x_change<0:
            angle+=180
        print(angle)
class Window:
    def __init__(self,x,y):
        self.width = x
        self.height = y
        self.ants = [ant()]
        self.food = (400,400)
        #creates pygame instance
        pygame.init()

        #fonts
        pygame.font.init()

        self.screen = pygame.display.set_mode((x,y))
        self.screen.fill((255,255,255))
        self.render()
        pygame.display.update()
    def input(self,action):
        return
    def tick(self):
        for ant in self.ants:
            ant.move_to_food(self.food)
    def render(self,object=None):
        pygame.draw.circle(self.screen,(0,255,0),self.food,5)
        for ant in self.ants:
            draw.circle(self.screen,(0,0,0),ant.pos,ant.r)
            ant.change_angle(0,self.screen)
        pygame.display.update()
def main():
    win = Window(600,600)
    win.tick()
    while True:
        for event in pygame.event.get():
            #if the player wants to quit the game.
            if event.type==pygame.QUIT:
                pygame.quit()
                exit()
            #left click
            if event.type ==pygame.MOUSEBUTTONDOWN and event.button==1:
                win.input(event.pos)
main()