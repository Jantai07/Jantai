class Animals:
    def __init__(self, name, age, weight, habitat, diet):
        self.name = name
        self.age = age
        self.weight = weight
        self.habitat = habitat
        self.diet = diet

    def eat(self):
        return f"{self.name} is eating {self.diet}."

    def sleep(self):
        return f"{self.name} is sleeping in the {self.habitat}."

    def make_sound(self):
        return f"{self.name} is making a sound."

    def move(self):
        return f"{self.name} is moving around."


class Reptiles(Animals):
    def __init__(self, name, age, weight, habitat, diet, length, venomous=None, scales_type=None):
        super().__init__(name, age, weight, habitat, diet)
        self.length = length
        self.venomous = venomous
        self.scales_type = scales_type

    def crawl(self):
        return f"{self.name} is crawling."

    def shed_skin(self):
        return f"{self.name} is shedding skin."

    def bask_in_sun(self):
        return f"{self.name} is basking in the sun."

    def lay_eggs(self):
        return f"{self.name} is laying eggs."


snake = Reptiles("Snake", 5, 12, "Rainforest", "Mice", 2.5, venomous=True, scales_type="Smooth")
lizard = Reptiles("Lizard", 3, 1.5, "Desert", "Insects", 0.5, scales_type="Rough")
turtle = Reptiles("Turtle", 100, 200, "Ocean", "Plants", 1.2, scales_type="Hard")

class Mammals(Animals):
    def __init__(self, name, age, weight, habitat, diet, strength=None, speed=None, jump_height=None):
        super().__init__(name, age, weight, habitat, diet)
        self.strength = strength
        self.speed = speed
        self.jump_height = jump_height

    def run(self):
        return f"{self.name} is running at {self.speed} km/h."

    def hunt(self):
        return f"{self.name} is hunting."

    def nurture_young(self):
        return f"{self.name} is nurturing its young."

    def communicate(self):
        return f"{self.name} is communicating with others."


lion = Mammals("Lion", 8, 190, "Savannah", "Meat", strength=500, speed=60)
elephant = Mammals("Elephant", 25, 6000, "Jungle", "Plants", strength=1000)
kangaroo = Mammals("Kangaroo", 6, 85, "Outback", "Grass", speed=40, jump_height=3)


class ZooShow:
    def __init__(self, show_name, ticket_price, animal_performer):
        self.show_name = show_name
        self.ticket_price = ticket_price
        self.animal_performer = animal_performer
        self.tickets_sold = 0

    def perform_show(self):
        if isinstance(self.animal_performer, Reptiles):
            return f"The reptile {self.animal_performer.name} is performing a trick by shedding its skin!"
        elif isinstance(self.animal_performer, Mammals):
            return f"The mammal {self.animal_performer.name} is performing an amazing jump of {self.animal_performer.jump_height} meters!"

    def display_info(self):
        return f"Show: {self.show_name}, Performer: {self.animal_performer.name}, Ticket Price: {self.ticket_price}."

    def sell_ticket(self, number_of_tickets):
        self.tickets_sold += number_of_tickets
        return f"{number_of_tickets} tickets sold."

    def calculate_revenue(self):
        revenue = self.ticket_price * self.tickets_sold
        return f"Total revenue: {revenue}."


zoo_show = ZooShow("Amazing Animal Show", 50, lion)
print(zoo_show.display_info())
print(zoo_show.perform_show())
print(zoo_show.sell_ticket(100))
print(zoo_show.calculate_revenue())
