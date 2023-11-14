from datetime import datetime


class Person:
    def __init__(self, name, email, dob, gender, favourite_teams):
        self.name = name
        self.email = email
        self.dob = dob
        self.gender = gender
        self.teams = favourite_teams

    def print_details(self):
        print(self.name)
        print(self.gender)
        print("------------TEAMS----------")

        for team in self.teams:
            print(team)
        print("-------------THE END-------")

    def cal_age(self):
        today = datetime.now()
        dob = datetime.strptime(self.dob, "%d-%m-%Y")
        delta = today - dob
        print(delta.days // 365, "Years Old")


person1 = Person("June", "Cosmaskaronei@gmail.com", "19-04-1996", "male", ["Man U", "Man City", "Chelsea"])
person1.print_details()
person1.cal_age()
