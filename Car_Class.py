class Car:

    def __init__(self, color, top_speed, price):
        self.color = color
        self.top_speed = top_speed
        self.curr_speed = 0
        self.price = price
        self.is_engine_on = False

    def start_engine(self):
        print("Engine is starting...")
        self.is_engine_on = True
        
    def turnoff_engine(self):
        print("Engine is turning off...")
        self.is_engine_on = False

    def accelerate(self):
        if self.is_engine_on:
            if self.curr_speed < self.top_speed:
                self.curr_speed += 10
            else:
                print("You are at top speed")
        else:
            print("Engine is off")

    def apply_breaks(self):
        if self.curr_speed > 0:
            self.curr_speed -= 10
        else:
            print("Current speed is already 0")

    def change_color(self, color):
        print("Color is changed from {} to {}".format(self.color, color))
        self.color = color

    def information(self):
        print("Color:", self.color)
        print("Current speed:", self.curr_speed)
        print("Top speed:", self.top_speed)
        print("Price:", self.price)


    
nano = Car("Red", 180, 150000)
nano.information()
nano.start_engine()
nano.accelerate()
nano.accelerate()
nano.accelerate()
nano.information()
nano.apply_breaks()
nano.apply_breaks()
nano.apply_breaks()
nano.apply_breaks()
nano.information()
nano.change_color("Black")
nano.information()
nano.turnoff_engine()
nano.accelerate()


