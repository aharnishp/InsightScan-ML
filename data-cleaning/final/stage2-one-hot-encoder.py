# read labels from data/labels2.csv
with open("data/labels2.csv", "r") as f:
    # read lines
    labellines = f.readlines()
    # split the lines by comma
    labellines = labellines[0].split(",")
    # remove the last element
    labellines = labellines[:-1]

# print(labellines)



# read file 
with open("data/ingridients-beauty.txt", "r") as f:
    # read lines
    lines = f.readlines()


# rows of one hot encoded data
# Format: Name of product, class, one hot encoded labels in order of labels2.csv
rows = []

# for each line
for line in lines:
    # split the line
    line = line.split(">>")
    if(len(line) < 2):
        continue
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

    onehot = ""

    for label in labellines:
        if(label in ingr):
            onehot += ",1"
        else:
            onehot += ",0"

        
    # check if the label exists in ingredients
    newLine = line[0] + "," + "1" + onehot + "\n"

    rows.append(newLine)
    

# read file 
with open("data/ingridients-food.txt", "r") as f:
    # read lines
    lines = f.readlines()

# for each line
for line in lines:
    # split the line
    line = line.split(">>")
    if(len(line) < 2):
        continue
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

    onehot = ""

    for label in labellines:
        if(label in ingr):
            onehot += ",1"
        else:
            onehot += ",0"

        
    # check if the label exists in ingredients
    newLine = line[0] + "," + "1" + onehot + "\n"

    rows.append(newLine)
    

# write the one hot encoded data to data/onehot.csv
with open("data/onehot.csv", "w") as f:
    # write headers
    f.write("Name,Class," + ",".join(labellines) + "\n")
    for row in rows:
        f.write(row)
