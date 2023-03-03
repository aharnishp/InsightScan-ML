dataFilePath = "data-cleaning/dataset/sample.md"

dataFile = open(dataFilePath)


include_Product_Name_in_Dataset = 1

dictionary = {}

ingdList = []

buf = []
for line in dataFile.readlines():
    if(len(line) > 2):
        ## Check if new ingridient has started
        if (line[1] == "." or line[2] == "."):
            # store product name
            # words = line.split(' ')
            # words 


            # store ingridients from buf to list
            ingdList.append(buf)
            buf = []
        else:
            spaceCount = line.count(' ')
            newLineCount = line.count('\n')

            # check if it has other character than space and new line
            if (spaceCount + newLineCount != len(line)):
                buf.append(line)

print(ingdList)