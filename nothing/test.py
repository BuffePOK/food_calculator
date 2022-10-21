import json

file = open("test.json","r+")

test = {
    "File":"test2.json",
    "User":{
        "name":"ita",
        "surname":"Hruchev",
        "age":5
    }
}

json.dump(test,file,indent=4)