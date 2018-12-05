import time
import os
file="E:\jw.org\jonah.mp4"
for k in range(3):
    time.sleep(1)
    if time.ctime=='Wed Oct 31 17:22:00 2018':
        os.system(file)
    else:
        print("the time is not available")
    
class Car:
    def __init__(self):
        self.engine=False
    def start_engine(self):
        print("starting the engine")
        self.engine=True
    def stop_engine(self):
        print("turning off the car")
        self.engine=False
    def drive(self):
        if self.engine:
            print("you are driving the car")
        else:
            print("you need to start the engine first")

class HondaCivic(Car):
    pass
