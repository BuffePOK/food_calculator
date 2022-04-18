# protein/fat/carbohydrates:
# Normal = 30/30/40
# Relief = 40/25/35
# Mass = 30/20/50
# 1 g of protein & carbohydrates = 4 calories
# 1 g of fats = 9 calories

def PCF(calories, koef_protein, koef_fat, koef_carbo):
    carbohydrates = int(calories * koef_carbo / 4)
    protein = int(calories * koef_protein / 4)
    fat = int(calories * koef_fat / 9)
    return protein, carbohydrates, fat

def main():
    from random import choices
    f1 = open("./tests/PCF.py_test.txt", "w")
    f1.write("PCF.py - test file\n\n")

    koefs = [(0.3,0.3,0.4), (0.4,0.25,0.35), (0.3,0.2,0.5), (0.45,0.2,0.35), (0.35,0.35,0.3), 
             (0.3,0.25,0.45), (0.4,0.35,0.25), (0.45,0.35,0.2), (0.25,0.25,0.5), (0.5,0.2,0.3)]

    for i in choices(koefs, k=5):
        for calories in choices(range(1000,6300,750), k=3):
            f1.write("Test: \nCalories = %d," % calories + " koef_protein = %.2f, koef_fat = %.2f, koef_carbo = %.2f.\n" % i)
            pcf = PCF(calories, i[0],i[1],i[2])
            f1.write("Done!\nProtein: %d, Fat: %d, Carbohydrates: %d\n\n\n" % pcf)
    f1.close()

if __name__ == "__main__":
    main()
