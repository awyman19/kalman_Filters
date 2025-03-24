import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random
class AModel:
    def __init__(self,F,B,x0,a,b,dt):
        self.F = F
        self.B = B
        self.X = x0
        self.z=[]
    def predict(self,u):
        self.X = np.array([np.matmul(self.F,self.X)+ np.matmul(self.B,u)])

    def add_measurement(self,z):
        self.z.append(z)
    def update(self):
        a=1/len(self.z)
        err=self.z[-1]-self.X[0]
        self.X = self.X + np.array([a*err])

class ABModel:
    def __init__(self,F,B,x0,a,b,dt):
        self.F = F
        self.B = B
        self.X = x0
        self.a = a
        self.b = b
        self.dt =dt
        #self.player_pos= [self.X[0],self.X[2]]
        self.z=[]
    def predict(self,u):
        self.X = np.matmul(self.F,self.X)+ np.matmul(self.B,u)

        #self.player_pos = [self.X[0], self.X[2]]
    def add_measurement(self,z):
        self.z.append(z)
    def update(self):
        err=self.z[-1]-self.X[0]
        self.X = self.X + np.array([self.a*err,self.b*(err/self.dt)])

x0 = np.array([30000,40])
dt=5
F = np.array([[1, dt],[0,1]])
B = np.eye(2)
u = np.zeros(2)
model = ABModel(F,B,x0,0.2,0.1,5)
trueModel = ABModel(F,B,x0,0.2,0.1,5)
#model.predict(u)
print(model.X)

prediction=[model.X]
estimate=[model.X]
true = [trueModel.X]
r=20
for n in range(r):
    print(n)
    z = random.normalvariate(trueModel.X[0], 150)
    model.add_measurement(z)
    model.update()
    true.append(trueModel.X)
    estimate.append(model.X)
    model.predict(u)
    prediction.append(model.X)
    trueModel.predict(u)
prediction= np.array(prediction)
true =np.array(true)
estimate = np.array(estimate)
print(prediction)
print(estimate)
print(true)
print(model.z)

plt.plot(list(range(r)),prediction[1:,0],list(range(r)),estimate[1:,0],list(range(r)),true[1:,0],list(range(r)),model.z)
plt.legend(['prediction','estimate','true state','measurement'])
plt.show()