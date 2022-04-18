from operator import ge
from calculators.calories import male, female
from calculators.PCF import PCF
from calculators.vitamins import vitamins
from users.users import add_user, delete_user, change_user_information
def main():
    name = "Dmitrii"
    surname = "Dichenko"
    age = 20
    height = 180
    weight = 80
    calories = male(weight, height,age)
    pcf = PCF(calories, 0.3,0.3,0.4)
    vitamine = vitamins(calories*1.5)

    user_json = {
                'name':name,
                'surname':surname,
                'age':age,
                'sex':"Male",
                'weight':weight,
                'height':height,
                'coefficients':{
                    'calories':calories*1.5,
                    'koef_protein':0.3,
                    'koef_fat':0.3,
                    'koef_carbo':0.4
                },
                'protein':pcf[0],
                'carbohydrates':pcf[1],
                'fats':pcf[2],
                'vitamins':vitamine,
            }
    
    change_user_information(user_json, user_json)

main()