class Car:

    def __init__(self):
        self.speed = 0
        self.odometer = 0
        self.time = 0

    def say_state(self):
        print("i'm going {} kph".format(self.speed))

    def accelerate(self):
        self.speed += 5

    def brake(self):
        self.speed -= 5

    def step(self):
        self.odometer += self.speed
        self.time += 1

    @property
    def average_speed(self):
        return self.odometer / self.time


if __name__ == '__main__':
    my_car = Car()
    print("i'm a car")
    while True:
        action = input("what should i do?").upper()
        if action not in "ABOS" or len(action) != 1:
            print("sdhjdhakj")
            continue
        if action == 'A':
            my_car.accelerate()
        elif action == 'B':
            my_car.brake()
        elif action == 'O':
            print("the car's average speed was {}".format(my_car.odometer))
        elif action == 'S':
            print("the car's average speed was {}".format(my_car.average_speed))
        my_car.step()
        my_car.say_state()
