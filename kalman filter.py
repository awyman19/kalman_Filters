import numpy as np
import random as rand
import pygame

pygame.init()
screen= pygame.display.set_mode((400,400))
clock = pygame.time.Clock()
running= True

#initialise positions and time
b=.9
dt =clock.tick(60)/1000
F= np.array([[1,dt,0,0],
             [0,b,0,0],
             [0,0,1,dt],
             [0,0,0,b]])
x=np.array([screen.get_width()/2,0,screen.get_height()/2,0])
speed=10
B= np.array([[0,0],
             [speed,0],
             [0,0],
             [0,speed]])

u=np.array([0,0])
player_pos= [x[0],x[2]] #start in center of

class Model:
    def __init__(self,F,B,x0):
        self.F = F
        self.B = B
        self.X = x0
        self.player_pos= [self.X[0],self.X[2]]
    def update(self,u):
        self.X = np.matmul(self.F,self.X)+ np.matmul(self.B,u)
        self.player_pos = [self.X[0], self.X[2]]


model= Model(F,B,x)
"""print(model.player_pos)
u[0]=1
model.update(u)
print(u,model.X)
u[0]=0
model.update(u)
print(u,model.X)

model.update(u)
print(u,model.X)
print(model.player_pos)"""
while running:
    #poll for events
    #pygame.QUIT means user closed window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")
    #pygame.draw.ellipse(screen, "red", unc_bound)
    model.update(u)
    print(model.X)
    u=np.array([0,0])
    pygame.draw.circle(screen, "orange", model.player_pos, 10)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        u[1] = -1

    if keys[pygame.K_s]:
        u[1] = 1

    if keys[pygame.K_a]:
        u[0] = -1

    if keys[pygame.K_d]:
        u[0] = 1


    pygame.display.flip()

    dt =clock.tick(60)/1000

"""
true_weight=100
noise=.1 #std dev

measurements=[rand.gauss(true_weight,noise) for i in range(10)]
print(measurements)
predicted=0

for i,measurement in enumerate(measurements):
    print(measurement,i+1)
    K=1/(i+1)
    predicted=predicted+K*(measurement-predicted)
    print(predicted)
"""

