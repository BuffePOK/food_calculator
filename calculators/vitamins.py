def vitamin_A(multiplier):
    minimum_low = 0.6
    minimum_high = 1.5
    maximum = 3.0
    if multiplier <= 1:
        vitamin = (minimum_high - minimum_low) * multiplier
        vitamin = minimum_low + vitamin

        return round(vitamin * 1.1, 2)

    elif multiplier > 1:
        vitamin = minimum_high * multiplier

        if vitamin > maximum: return round(maximum * 1.1, 2)

        return round(vitamin * 1.1, 2)

def vitamin_B1(multiplier):
    minimum_low = 0.9
    minimum_high = 2.0
    # maximum = "No limit"
    if multiplier <= 1:
        vitamin = (minimum_high - minimum_low) * multiplier
        vitamin = minimum_low + vitamin

        return round(vitamin * 1.1, 2)

    elif multiplier > 1:
        vitamin = minimum_high * multiplier

        # if vitamin > maximum: return round(maximum * 1.1, 2)

        return round(vitamin * 1.1, 2)

def vitamin_B2(multiplier):
    minimum_low = 1.1
    minimum_high = 2.8
    # maximum = "No limit"
    if multiplier <= 1:
        vitamin = (minimum_high - minimum_low) * multiplier
        vitamin = minimum_low + vitamin

        return round(vitamin * 1.1, 2)

    elif multiplier > 1:
        vitamin = minimum_high * multiplier

        # if vitamin > maximum: return round(maximum * 1.1, 2)
        
        return round(vitamin * 1.1, 2)

def vitamin_B3(multiplier):
    minimum_low = 11.0
    minimum_high = 25.0
    maximum = 60.0
    if multiplier <= 1:
        vitamin = (minimum_high - minimum_low) * multiplier
        vitamin = minimum_low + vitamin

        return round(vitamin * 1.1, 2)

    elif multiplier > 1:
        vitamin = minimum_high * multiplier

        if vitamin > maximum: return round(maximum * 1.1, 2)
        
        return round(vitamin * 1.1, 2)

def vitamin_B4(multiplier):
    minimum_low = 500.0
    minimum_high = 1000.0
    maximum = 3000.0
    if multiplier <= 1:
        vitamin = (minimum_high - minimum_low) * multiplier
        vitamin = minimum_low + vitamin

        return round(vitamin * 1.1, 2)

    elif multiplier > 1:
        vitamin = minimum_high * multiplier

        if vitamin > maximum: return round(maximum * 1.1, 2)
        
        return round(vitamin * 1.1, 2)

def vitamin_B5(multiplier):
    minimum_low = 4.0
    minimum_high = 12.0
    # maximum = "No limit"
    if multiplier <= 1:
        vitamin = (minimum_high - minimum_low) * multiplier
        vitamin = minimum_low + vitamin

        return round(vitamin * 1.1, 2)

    elif multiplier > 1:
        vitamin = minimum_high * multiplier

        # if vitamin > maximum: return round(maximum * 1.1, 2)
        
        return round(vitamin * 1.1, 2)

def vitamin_B6(multiplier):
    minimum_low = 1.1
    minimum_high = 2.6
    maximum = 25.0
    if multiplier <= 1:
        vitamin = (minimum_high - minimum_low) * multiplier
        vitamin = minimum_low + vitamin

        return round(vitamin * 1.1, 2)

    elif multiplier > 1:
        vitamin = minimum_high * multiplier

        if vitamin > maximum: return round(maximum * 1.1, 2)
        
        return round(vitamin * 1.1, 2)

def vitamin_B9(multiplier):
    minimum_low = 0.5
    minimum_high = 0.8
    # maximum = "No limit"
    if multiplier <= 1:
        vitamin = (minimum_high - minimum_low) * multiplier
        vitamin = minimum_low + vitamin

        return round(vitamin * 1.1, 2)

    elif multiplier > 1:
        vitamin = minimum_high * multiplier

        # if vitamin > maximum: return round(maximum * 1.1, 2)
        
        return round(vitamin * 1.1, 2)

def vitamin_B12(multiplier):
    minimum_low = 1.4
    minimum_high = 3.0
    # maximum = "No limit"
    if multiplier <= 1:
        vitamin = (minimum_high - minimum_low) * multiplier
        vitamin = minimum_low + vitamin

        return round(vitamin * 1.1, 2)

    elif multiplier > 1:
        vitamin = minimum_high * multiplier

        # if vitamin > maximum: return round(maximum * 1.1, 2)
        
        return round(vitamin * 1.1, 2)

def vitamin_C(multiplier):
    minimum_low = 45.0
    minimum_high = 110.0
    maximum = 2000.0
    if multiplier <= 1:
        vitamin = (minimum_high - minimum_low) * multiplier
        vitamin = minimum_low + vitamin

        return round(vitamin * 1.1, 2)

    elif multiplier > 1:
        vitamin = minimum_high * multiplier

        if vitamin > maximum: return round(maximum * 1.1, 2)
        
        return round(vitamin * 1.1, 2)

def vitamin_D(multiplier):
    minimum_low = 0.01
    minimum_high = 0.02
    maximum = 0.05
    if multiplier <= 1:
        vitamin = (minimum_high - minimum_low) * multiplier
        vitamin = minimum_low + vitamin

        return round(vitamin * 1.1, 2)

    elif multiplier > 1:
        vitamin = minimum_high * multiplier

        if vitamin > maximum: return round(maximum * 1.1, 2)
        
        return round(vitamin * 1.1, 2)

def vitamin_E(multiplier):
    minimum_low = 7.0
    minimum_high = 25.0
    maximum = 300.0
    if multiplier <= 1:
        vitamin = (minimum_high - minimum_low) * multiplier
        vitamin = minimum_low + vitamin

        return round(vitamin * 1.1, 2)

    elif multiplier > 1:
        vitamin = minimum_high * multiplier

        if vitamin > maximum: return round(maximum * 1.1, 2)
        
        return round(vitamin * 1.1, 2)

def vitamin_K(multiplier):
    minimum_low = 0.05
    minimum_high = 0.15
    # maximum = "No limit"
    if multiplier <= 1:
        vitamin = (minimum_high - minimum_low) * multiplier
        vitamin = minimum_low + vitamin

        return round(vitamin * 1.1, 2)

    elif multiplier > 1:
        vitamin = minimum_high * multiplier

        # if vitamin > maximum: return round(maximum * 1.1, 2)
        
        return round(vitamin * 1.1, 2)

def vitamin_H(multiplier):
    minimum_low = 0.02
    minimum_high = 0.1
    # maximum = "No limit"
    if multiplier <= 1:
        vitamin = (minimum_high - minimum_low) * multiplier
        vitamin = minimum_low + vitamin

        return round(vitamin * 1.1, 2)

    elif multiplier > 1:
        vitamin = minimum_high * multiplier

        # if vitamin > maximum: return round(maximum * 1.1, 2)
        
        return round(vitamin * 1.1, 2)

def element_Fe(multiplier):
    minimum_low = 10.0
    minimum_high = 22.0
    # maximum = "No limit"
    if multiplier <= 1:
        vitamin = (minimum_high - minimum_low) * multiplier
        vitamin = minimum_low + vitamin

        return round(vitamin * 1.1, 2)

    elif multiplier > 1:
        vitamin = minimum_high * multiplier

        # if vitamin > maximum: return round(maximum * 1.1, 2)
        
        return round(vitamin * 1.1, 2)

def element_Mg(multiplier):
    minimum_low = 200.0
    minimum_high = 500.0
    # maximum = "No limit"
    if multiplier <= 1:
        vitamin = (minimum_high - minimum_low) * multiplier
        vitamin = minimum_low + vitamin

        return round(vitamin * 1.1, 2)

    elif multiplier > 1:
        vitamin = minimum_high * multiplier

        # if vitamin > maximum: return round(maximum * 1.1, 2)
        
        return round(vitamin * 1.1, 2)

def element_Cu(multiplier):
    minimum_low = 0.9
    minimum_high = 3.0
    maximum = 5.0
    if multiplier <= 1:
        vitamin = (minimum_high - minimum_low) * multiplier
        vitamin = minimum_low + vitamin

        return round(vitamin * 1.1, 2)

    elif multiplier > 1:
        vitamin = minimum_high * multiplier

        if vitamin > maximum: return round(maximum * 1.1, 2)
        
        return round(vitamin * 1.1, 2)

def element_Ca(multiplier):
    minimum_low = 500.0 
    minimum_high = 1200.0
    maximum = 2500.0
    if multiplier <= 1:
        vitamin = (minimum_high - minimum_low) * multiplier
        vitamin = minimum_low + vitamin

        return round(vitamin * 1.1, 2)

    elif multiplier > 1:
        vitamin = minimum_high * multiplier

        if vitamin > maximum: return round(maximum * 1.1, 2)
        
        return round(vitamin * 1.1, 2)

def element_P(multiplier):
    minimum_low = 550.0
    minimum_high = 1400.0
    # maximum = "No limit"
    if multiplier <= 1:
        vitamin = (minimum_high - minimum_low) * multiplier
        vitamin = minimum_low + vitamin

        return round(vitamin * 1.1, 2)

    elif multiplier > 1:
        vitamin = minimum_high * multiplier

        # if vitamin > maximum: return round(maximum * 1.1, 2)
        
        return round(vitamin * 1.1, 2)

def element_Zn(multiplier):
    minimum_low = 10.0
    minimum_high = 15.0
    maximum = 25.0
    if multiplier <= 1:
        vitamin = (minimum_high - minimum_low) * multiplier
        vitamin = minimum_low + vitamin

        return round(vitamin * 1.1, 2)

    elif multiplier > 1:
        vitamin = minimum_high * multiplier

        if vitamin > maximum: return round(maximum * 1.1, 2)
        
        return round(vitamin * 1.1, 2)

def element_Se(multiplier):
    minimum_low = 0.03
    minimum_high = 0.08
    maximum = 0.3
    if multiplier <= 1:
        vitamin = (minimum_high - minimum_low) * multiplier
        vitamin = minimum_low + vitamin

        return round(vitamin * 1.1, 2)

    elif multiplier > 1:
        vitamin = minimum_high * multiplier

        if vitamin > maximum: return round(maximum * 1.1, 2)
        
        return round(vitamin * 1.1, 2)

def element_I(multiplier):
    minimum_low = 0.1 
    minimum_high = 0.2
    maximum = 0.6
    if multiplier <= 1:
        vitamin = (minimum_high - minimum_low) * multiplier
        vitamin = minimum_low + vitamin

        return round(vitamin * 1.1, 2)

    elif multiplier > 1:
        vitamin = minimum_high * multiplier

        if vitamin > maximum: return round(maximum * 1.1, 2)
        
        return round(vitamin * 1.1, 2)

def element_Cr(multiplier):
    minimum_low = 0.03
    minimum_high = 0.1
    # maximum = "No limit"
    if multiplier <= 1:
        vitamin = (minimum_high - minimum_low) * multiplier
        vitamin = minimum_low + vitamin

        return round(vitamin * 1.1, 2)

    elif multiplier > 1:
        vitamin = minimum_high * multiplier

        # if vitamin > maximum: return round(maximum * 1.1, 2)
        
        return round(vitamin * 1.1, 2)

def element_Mn(multiplier):
    minimum_low = 2.0
    minimum_high = 5.0
    maximum = 5.0
    if multiplier <= 1:
        vitamin = (minimum_high - minimum_low) * multiplier
        vitamin = minimum_low + vitamin

        return round(vitamin * 1.1, 2)

    elif multiplier > 1:
        vitamin = minimum_high * multiplier

        if vitamin > maximum: return round(maximum * 1.1, 2)
        
        return round(vitamin * 1.1, 2)

def element_Mo(multiplier):
    minimum_low = 0.05
    minimum_high = 0.1
    maximum = 0.6
    if multiplier <= 1:
        vitamin = (minimum_high - minimum_low) * multiplier
        vitamin = minimum_low + vitamin

        return round(vitamin * 1.1, 2)

    elif multiplier > 1:
        vitamin = minimum_high * multiplier

        if vitamin > maximum: return round(maximum * 1.1, 2)
        
        return round(vitamin * 1.1, 2)



def multiply(calories):
    min_calories = 1300
    max_calories = 2200

    if calories < min_calories: return 0

    elif calories >= min_calories and calories <= max_calories:
        calories = calories - min_calories
        max_calories = max_calories - min_calories

        return calories / max_calories

    elif calories > max_calories: return calories / max_calories

def vitamins(calories):
    multiplier = multiply(calories)
    vitamins_dict = {
                      "A": vitamin_A(multiplier),
                      "B1": vitamin_B1(multiplier),
                      "B2": vitamin_B2(multiplier),
                      "B3": vitamin_B3(multiplier),
                      "B4": vitamin_B4(multiplier),
                      "B5": vitamin_B5(multiplier),
                      "B6": vitamin_B6(multiplier),
                      "B9": vitamin_B9(multiplier),
                      "B12": vitamin_B12(multiplier),
                      "C": vitamin_C(multiplier),
                      "D": vitamin_D(multiplier),
                      "E": vitamin_E(multiplier),
                      "K": vitamin_K(multiplier),
                      "H": vitamin_H(multiplier),
                      "Fe": element_Fe(multiplier),
                      "Mg": element_Mg(multiplier),
                      "Cu": element_Cu(multiplier),
                      "Ca": element_Ca(multiplier),
                      "P": element_P(multiplier),
                      "Zn": element_Zn(multiplier),
                      "Se": element_Se(multiplier),
                      "I": element_I(multiplier),
                      "Cr": element_Cr(multiplier),
                      "Mn": element_Mn(multiplier),
                      "Mo": element_Mo(multiplier)
    }
    return vitamins_dict

def main():
    file = open("./tests/vitamins.py_test.txt",'w')
    file.write("vitamins.py - test file\n")
    for i in range(1000,6300,750):
        test = vitamins(i)
        file.write("Vitamins [calories = %d]\n" % i)
        for j in test:
            file.write(j + " : " + str(test[j]) + "\n")
        file.write("\n\n")

    file.close()

if __name__ == "__main__":
    main()