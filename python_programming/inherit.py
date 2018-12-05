class Car:
    def __init__(self):
        self.engine='False'
    def start_engine(self):
        print("starting the engine")
        self.engine='True'
    def stop_engine(self):
        print("turning off the car")
        self.engine='False'
    def drive(self):
        if self.engine =="true":
            print("you are driving the car")
        else:
            print("you need to start the engine first")

class HondaCivic(Car):
    pass
