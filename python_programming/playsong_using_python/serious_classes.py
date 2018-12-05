class Car:
    def __init__(self,color,model):
        self.color=color
        self.model=model
        self.engine="off"
    def start_engine(self):
        if self.engine=="off":
            print("starting the engine")
            self.engine="on"
        else:
            print("the engine is running already")
    def stop_engine(self):
        if self.engine=="on":
            print("stopping the engine")
            self.engine=="off"
        else:
            print("the enginne is already down")
    def drive(self):
        if self.engine=="on":
            print("starting to drive")
        else:
            print("the engine needs to be started first")
    def display(self):
        print(self.color)
        print(self.model)
        print("the engine is ",self.engine)

        
mycar=Car(str(input("enter the color of a car")),str(input("enter the model of car")))
class Honda(Car):
    model='honda'
newcar=Car("jonathan","nshuti")
newcars=Honda("munene","kk")
print(newcar.model)
print(newcars.model)
#print(mycar.color)
#print(mycar.model)
#mycar.display()
#mycar.start_engine()
#mycar.drive()

