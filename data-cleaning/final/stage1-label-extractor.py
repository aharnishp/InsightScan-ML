
labelDict = {}
labelSet = set()

# extract labels from the data
# open file data/ingridients-beauty.txt
with open("data/ingridients-beauty.txt", "r") as f:
    # read lines
    lines = f.readlines()
# for each line
for line in lines:
    # split the line
    line = line.split(">>")
    ingr = line[1]
    # split the ingredients by comma
    ingr = ingr.lower().replace("\n"," ").replace("\t"," ").replace("("," ").replace("."," ").replace(")"," ").replace('"','').replace('*','').replace("["," ").replace("]"," ").replace("ii"," ").replace("iii"," ").split(",")
    
    # for each ingredient
    for i in ingr:
        # split by space
        i = i.split(" ")

        # remove only numeric elements
        i = [x for x in i if not x.isdigit()]

        # remove elements ending with %
        i = [x for x in i if not x.endswith("%")]
        i = [x for x in i if not x.endswith("ml")]
        i = [x for x in i if not x.endswith("g")]
        i = [x for x in i if not x.endswith("gm")]
        
        # increase count of label if exists
        for j in i:
            if j in labelDict:
                labelDict[j] += 1
            else:
                labelDict[j] = 1
        







# sort the labels by count
labelDict = sorted(labelDict.items(), key=lambda x: x[1], reverse=True)

# store labels in data/labels2.txt
with open("data/labels2.csv", "w") as f:
    for i in labelDict:
        if(len(i[0]) >= 4):
            f.write(i[0] + ",")
            # f.write(i[0] + " " + str(i[1]) + "\n")