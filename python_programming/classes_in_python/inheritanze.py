class Car:
    def __init__(self):
        self.engine=False
    def start_engine(self):
        print("starting the car")
        self.engine=True
    def stop_engine(self):
        print("turning off the car")
        self.engine=False
    def drive(self):
        if self.engine==False:
            print("starting the car")
        else:
            print("the car is running")
        
class BlueCar:
    color='blue'
        
class Honda(Car,BlueCar):
    model='honda'
    def start_engine(self):
        super().start_engine()
        print("honda! start engine")
class Hondacivic(Honda):
    model='honda civic'
car=Hondacivic()
car.stop_engine()
  

