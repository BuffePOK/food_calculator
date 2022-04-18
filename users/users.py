import json
from errors import ChangeUserInformationError, UserNotExist, UserExistsExeption
from os import remove
from copy import deepcopy


def read_users_list():
    try:
        file = open("./users/users_list.json")
        users_list = json.load(file)
        return users_list
    except (FileNotFoundError, json.JSONDecodeError):
        file = open("./users/users_list.json",'w')

        dict_example = {}
        json.dump(dict_example, file, indent=4)

        file.close()
        return read_users_list()


def add_user(user_information):

    users_list = read_users_list()

    for i in users_list:
        if users_list[i]["name"] == user_information["name"] and users_list[i]["surname"] == user_information["surname"]:
            raise UserExistsExeption("This user already exists")

    json_file = user_information["name"] + "_" + user_information["surname"] + ".json"
    user_id = len(users_list)

    add_user_list = {
    'name' : user_information["name"],
    'surname' : user_information["surname"],
    'json' : json_file
    }
    users_list[user_id] = add_user_list

    file = open("./users/users_list.json","w")
    json.dump(users_list, file, indent=4)
    file.close()

    file = open("./users/" + json_file, 'w')
    user_information["id"] = user_id
    json.dump(user_information, file, indent = 4)
    file.close()

def delete_user(user_information):
    users_list = read_users_list()
    copy_users_list = deepcopy(users_list)

    success = False

    for i in copy_users_list:
        if users_list[i]["name"] == user_information["name"] and users_list[i]["surname"] == user_information["surname"]:
            remove("./users/" + users_list[i]["json"])
            del users_list[i]

            file = open("./users/users_list.json","w")
            json.dump(users_list, file, indent=4)
            file.close()

            success = True
    if not success: 
        raise UserNotExist("The user does not exist")

def change_user_information(old_user_information, new_user_information):
    users_list = read_users_list()
    
    try:
        delete_user(old_user_information)
    except UserNotExist:
        raise ChangeUserInformationError("Delete user Error")

    try:
        add_user(new_user_information)
    except UserExistsExeption:
        add_user(old_user_information)
        raise ChangeUserInformationError("Add user Error")
