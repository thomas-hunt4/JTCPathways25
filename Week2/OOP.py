# OOP ***********************************************
# difference between procedural and Object Oriented Programming




# initializing a class

class Restaurant:


    def __init__(self, name):
        self.name = name
        self.address = []
        self.menu = ''
        self.hours = {
            'Sunday': [0, 0],
            'Monday': [0, 0],
            'Tuesday': [0, 0],
            'Wednesday': [0, 0],
            'Thursday': [0, 0],
            'Friday': [0, 0],
            'Saturday': [0, 0],

        }

    def update_hours(self, day, opening, closing):
            hours_for_day = self.hours[day]
            hours_for_day[0] = opening
            hours_for_day[1] = closing

    def is_open(self, day, time):
        hours_for_day = self.hours[day]
        return hours_for_day[0] < time < hours_for_day[1]

    


islands = Restaurant('Islands')

spudz = Restaurant('Spudz')


islands.update_hours("Wednesday", 8, 19)




        pass