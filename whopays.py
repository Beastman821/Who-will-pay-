import random

names_strings = input("give me everybody's names, seperated by a comma. ")
names = names_strings.split(",")
    
num_items = len(names)

random_choice = random.randint(0, num_items - 1)
person_who_will_pay = names[random_choice]
print(person_who_will_pay + " is going to buy the meal today.")