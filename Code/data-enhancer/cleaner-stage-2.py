import openai
import time

# read file cleaned-ingreidients.txt

with open('data-enhancer/cleaned-ingridients-food.txt') as file1:
    file_contents = file1.read()

lines = file_contents.split('\n')

with open("data-enhancer/chat-gpt.key", "r") as f2:
    key = f2.read()
    openai.api_key = key


# create an empty file to append the responses to
with open("data-enhancer/cleaned-ingridients-2.txt", "w") as f:
    pass



newlines = []
for line in lines:
    newele = []
    elements = line.split(',')
    for element in elements:
        if(element.__contains__("ngredient")):
            continue
        else:
            newele.append(element)

    newlines.append(newele)

print(newlines)

# save to file
with open("data-enhancer/cleaned-ingridients-2.txt", "a") as f:
    for line in newlines:
        f.write(','.join(line) + '\n')