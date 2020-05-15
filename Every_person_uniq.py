from datetime import datetime, date

class Person:
    def __init__(self, first_name, last_name, birth_date, job, working_years, salary, country, city, gender='unknown'):

        self.name_cust = first_name
        self.f_name = last_name
        self.bd = birth_date
        self.job = job
        self.working = working_years
        self.salary = salary
        self.country = country
        self.city = city
        self.gender = gender

        # raise NotImplementedError

    def name(self):
        print(f"{self.name_cust} {self.f_name}")
        return f"{self.name_cust} {self.f_name}"

    def age(self):
        bd_cust = datetime.strptime(self.bd, "%d.%m.%Y")
        # date_now = datetime.today()
        date_now = date(2018, 1, 1)
        delta = date_now.year - bd_cust.year - ((date_now.month, date_now.day) < (bd_cust.month, bd_cust.day))
        print(delta)
        return delta

    def work(self):
        if self.gender == "male":
            prefix = "He is"
        elif self.gender == "female":
            prefix = "She is"
        else:
            prefix = "Is"
        print(f"{prefix} a {self.job}")
        return f"{prefix} a {self.job}"

    def money(self):
        money_cost = str(self.working * self.salary * 12)
        new_money_cost = ""
        for idx, val in enumerate(money_cost[::-1]):
            if idx in range(3, len(money_cost)+1, 3):
                new_money_cost += " " + val
            else:
                new_money_cost += val
        print(new_money_cost[::-1])
        return new_money_cost[::-1]

    def home(self):
        print(f"Lives in {self.city}, {self.country}")
        return f"Lives in {self.city}, {self.country}"


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    p1 = Person("John", "Smith", "19.09.1979", "welder", 15, 3600, "Canada", "Vancouver", "male")
    p2 = Person("Hanna Rose", "May", "05.12.1995", "designer", 2.2, 2150, "Austria", "Vienna")
    p3 = Person('Kate', 'Hound', '05.02.2000', 'student', 0, 0, 'Australia', 'Sydney', 'female')
    assert p1.name() == "John Smith", "Name"
    assert p1.age() == 38, "Age"
    assert p2.work() == "Is a designer", "Job"
    assert p1.money() == "648 000", "Money"
    assert p2.home() == "Lives in Vienna, Austria", "Home"
    assert p3.work() == "She is a student"
    print("Coding complete? Let's try tests!")
