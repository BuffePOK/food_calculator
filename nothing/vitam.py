import copy


class Vitamines():
    def __init__(self, name ,good = [], bad = []):
        self.name = name
        self.good = good
        self.bad = bad

    def __repr__(self):
        return "[Vitamines: %s]" % self.name

    def isNeutral(self, vitamine):
        if vitamine not in self.good and vitamine not in self.bad:
            return True
        else: return False


vitamines_good = {
                  "A": ['C','E', 'Fe', 'Zn'],
                  "B1" : ['B5'],
                  "B2" : ['B3', "B5", 'B6', 'B9', 'K', "Zn"],
                  "B3" : ['B2', 'B6', 'Fe'],
                  "B4" : ['B9', 'B12'],
                  'B5' : ['B1','B2','B6','B9','B12'],
                  "B6" : ['B2','B3','Cu','Ca','Zn'],
                  "B9" : ['B2','B4','B5','B12','C'],
                  "B12" : ['B4','B5','B9','Ca'],
                  "C" : ['C','B5','B9','E','Fe','Ca'],
                  "D" : ['Ca','P'],
                  "E" : ['A','C','Se'],
                  "K" : ['B2','Ca'],
                  "H" : ['Mg'],
                  "Fe" : ['A','B3','C','Cu'],
                  "Mg" : ['H','Ca'],
                  "Cu" : ['B6','Fe','I'],
                  "Ca" : ['B6','B12','C','D','K','Mg'],
                  "P" : ['D'],
                  "Zn" : ['A','B2','B6','I'],
                  "Se" : ['E','I'],
                  "I" : ['Cu','Zn','Se'],
                  "Cr" : [None],
                  "Mn" : [None],
                  "Mo" : [None]
}

vitamines_bad = {
                 "A": ["B12",'K'],
                 "B1" : ["B2",'B3','B4','B6','B12','C','Mg','Ca'],
                 "B2" : ['B1','B12','Fe','Cu'],
                 "B3" : ['B1'],
                 "B4" : ['B1'],
                 'B5' : ['Cu'],
                 "B6" : ['B1','B12'],
                 "B9" : ['Zn'],
                 "B12" : ['A','B1','B2','B6','C','E','Fe','Cu','Mo'],
                 "C" : ['B1','B12','Cu'],
                 "D" : ['E'],
                 "E" : ['B12','D','K','Fe','Mg','Cu','Zn'],
                 "K" : ['A','E'],
                 "H" : [None],
                 "Fe" : ['B2','B12','E','Mg','Ca','Zn','Cr','Mn'],
                 "Mg" : ['B1','E','Fe','P','I'],
                 "Cu" : ['B2','B5','B12','C','E','Zn','Se','Mo'],
                 "Ca" : ['B1','Fe','P','Zn','I','Cr','Mn'],
                 "P" : ['Mg','Ca','Mn'],
                 "Zn" : ['B9','E','Fe','Cu','Ca','Cr'],
                 "Se" : ['Cu'],
                 "I" : ['Mg','Ca','Mn'],
                 "Cr" : ['Fe','Ca','Zn'],
                 "Mn" : ['Fe','Ca','P','I'],
                 "Mo" : ['B12','Cu']
}

vitamines = ["A", "B1", "B2", "B3", "B4", "B5", "B6", "B9", "B12", "C", "D", "E", "K", "H", "Fe", "Mg", "Cu", "Ca", "P", "Zn", "Se", "I", "Cr", "Mn", "Mo"]


vit_class = []

for i in vitamines_good:
    vit_class.append(Vitamines(i))

for i in vit_class:
    i.good = vitamines_good[i.name]
    i.bad = vitamines_bad[i.name]

vit_class_copy = copy.deepcopy(vit_class)

ans_dict = {}


for vitamine_name in vit_class:
    file = open("./vitamines/" + vitamine_name.name + ".txt", 'w')

    answer = []


    for i in vit_class_copy:
        vitamine_good_ans = []
        vitamine_bad_ans = []

        for j in i.bad:
            if j != None:
                vitamine_bad_ans.append(j)

        for j in vit_class_copy:
            if j.name not in vitamine_bad_ans and j.name not in vitamine_good_ans and j != None:
                vitamine_good_ans.append(j.name)
                for z in j.bad:
                    if z != None and z not in vitamine_bad_ans:
                        vitamine_bad_ans.append(z)

        if vitamine_good_ans not in answer:
            ans_dict[str(i.name)] = vitamine_good_ans



        answer.append(i.name)
        answer.append(vitamine_good_ans)
        answer.append(vitamine_bad_ans)
                


        good_ans_str = ""
        bad_ans_str = ""
        for z in vitamine_good_ans:
            good_ans_str += str(z) + ", "

        for z in vitamine_bad_ans:
            bad_ans_str += str(z) + ", "

        file.write("[" + i.name + "]" + " Good ans: ")
        file.write(good_ans_str + "\n")
        # file.write("[" + i.name + "]" + " Bad ans: ")
        # file.write(bad_ans_str + "\n")

    transit = vit_class_copy[0]
    del vit_class_copy[0]
    vit_class_copy.append(transit)

    print(answer)

    file.close()
    break


print(ans_dict)

file = open('vitamine.txt','w')

for i in ans_dict:
    vit_ans = ""
    for j in ans_dict[i]:
        vit_ans += j + ", "
    file.write("[" + i + "]: " + vit_ans + '\n')

file.close()

# vit_class = []

# for i in vitamines_good:
#     vit_class.append(Vitamines(i))

# for i in vit_class:
#     i.good = vitamines_good[i.name]
#     i.bad = vitamines_bad[i.name]

# answer = []


# for i in vit_class:
#     vitamine_good_ans = []
#     vitamine_bad_ans = []

#     for j in i.bad:
#         vitamine_bad_ans.append(j)

#     for j in i.good:
#         if j not in vitamine_good_ans and j not in vitamine_bad_ans:
#             vitamine_good_ans.append(j)
#             for z in vit_class:
#                 if z.name == j:
#                     for ll in z.bad:
#                         vitamine_bad_ans.append(ll)
#     answer.append(i.name)
#     answer.append(vitamine_good_ans)

