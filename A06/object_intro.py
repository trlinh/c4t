class Dog:
    def __init__(self, name, age, breed, weight):
        self.name = name 
        self.age = age
        self.breed = breed
        self.weight= weight
    
    def eat(self):
        self.weight +=0.1

class Clock:
    def __init__(self, seconds, minutes, hours):
        self.seconds = seconds
        self.minutes = minutes
        self.hours = hours
    
    def display(self):
        print(self.hours, ":", self.minutes, ":", self.seconds, sep="")
    
    def tick(self):
        self.seconds +=1
        if self.seconds==60:
            self.minutes+=1
            self.seconds=0
        if self.minutes==60:
            self.hours+=1
            self.minutes=0
        if self.hours==12:
            clock.reset()
    
    def reset(self):
        self.seconds=0
        self.minutes=0
        self.hours=0

clock = Clock(59,59,11)
clock.tick()
clock.tick()
clock.display()

    
