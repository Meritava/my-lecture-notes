BONUS_RATE = 0.3

user_input = input("what is your name?")
user_salary = float(input("What is your salary"))

def calculate_bonus(value):
    bonus = value * BONUS_RATE
    return bonus

def greetings(name, salary):
    print("function called", end="\n")
    print("Hello {name}".format(name=name)) #print("Hello")
    user_bonus = calculate_bonus(salary)
    print("The bonus calculated on your salary {} is {}".format(salary, user_bonus))
greetings(user_input, user_salary)
