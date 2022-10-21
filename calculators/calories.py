# calorie calculator

from random import randint


def female_Mifflin(weight, height, age): # Mifflin – San Jeoru Formula for female
    return 10 * weight + 6.25 * height - 5 * age - 161

def female_Harris(weight, height, age): # The Harris-Benedict Formula for female
    return 665.1 + 9.563 * weight + 1.85 * height - 4.676 * age

def male_Mifflin(weight, height, age): # Mifflin – San Jeoru Formula for male
    return 10 * weight + 6.25 * height - 5 * age + 5

def male_Harris(weight, height, age): # The Harris-Benedict Formula for male
    return 66.5 + 13.75 * weight + 5.003 * height - 6.775 * age

def female(weight, height, age):
    calories = (female_Mifflin(weight, height, age), female_Harris(weight, height, age))
    return int(sum(calories)/len(calories))

def male(weight, height, age):
    calories = (male_Mifflin(weight, height, age), male_Harris(weight, height, age))
    return int(sum(calories)/len(calories))


def main():  # to check
    file = open("./tests/calories.py_test.txt", "w")
    file.write("calories.py - test file\n\n")
    for never in range(15):
        weight = randint(65,200)
        height = randint(160,225)
        age = randint(18, 75)
        file.write("Test. Male. \n Weight = %d, Height = %d, Age = %d.\n" % (weight, height, age))
        calories = male(weight,height,age)
        file.write("Calories: %d\n\n" % calories)

    for never in range(15):
        weight = randint(55,140)
        height = randint(150,200)
        age = randint(18, 75)
        file.write("Test. Female. \n Weight = %d, Height = %d, Age = %d.\n" % (weight, height, age))
        calories = female(weight,height,age)
        file.write("Calories: %d\n\n" % calories)

if __name__ == "__main__":
    main()