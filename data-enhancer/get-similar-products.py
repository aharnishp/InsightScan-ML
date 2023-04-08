import openai
import time

# This script takes in a list of items from the dataset and asks ChatGPT about 10 relevant items for each of them


# Set up OpenAI API credentials
# read value from a file and set it as the API key
with open("data-enhancer/chat-gpt.key", "r") as f:
    key = f.read()
    openai.api_key = key
# print(key, type(key))



# create an empty file to append the responses to
with open("data-enhancer/chat-gpt-responses.txt", "w") as f:
    pass




existingItems = ""
# open file data-cleaning/dataset/sample.md and read the contents
with open("data-cleaning/dataset/sample2.md", "r") as f:
    existingItems = f.read()

# split the contents by newline
existingItems = existingItems.split("\n")

# # check if line has ". "
# existingItems = [x for x in existingItems if ". " in x]


newList = []

for line in existingItems:
    if(". " in line):
        if(line.split(".")[0].isdigit()):
            print(line)
            print(line.split(".")[1])
            newList.append(line.split(".")[1])

existingItems = newList
# strip whitespace
existingItems = [x.strip() for x in existingItems]

# remove empty strings
existingItems = list(filter(None, existingItems))

# remove duplicates
existingItems = list(dict.fromkeys(existingItems))

# print(existingItems)

# Define your list of items to ask ChatGPT about
items = existingItems
# items = ["Amul Butter", "Cadbury Dairy Milk Silk - Bubbly", "Haldiram's Moong Dal", "Maggi 2-Minute Noodles - Masala"]
# items = [] #["Amul Butter", "Cadbury Dairy Milk Silk - Bubbly", "Haldiram's Moong Dal", "Maggi 2-Minute Noodles - Masala"]

# Loop through each item in the list and ask ChatGPT
for item in items:
    # Define your prompt for ChatGPT
    prompt = "List comma separated list of 10 food product names which are similar to the food product " + str(item)

    print("prompt: ", prompt)

    # Call the OpenAI GPT-3 API to generate a response
    response = openai.Completion.create(
        # engine="gpt-3.5-turbo",
        engine="davinci-instruct-beta",
        # engine="ada-instruct-beta",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.75,
    )


    print("Raw response: ", response.choices[0].text)

    # similar_products = response.choices[0].text.replace("-", "").split("\n")
    similar_products = response.choices[0].text.split("\n")
    
    similar_products = similar_products[1:]

    # split all elements in the list by comma
    similar_products = [x.split(",") for x in similar_products]

    # flatten the list
    similar_products = [item for sublist in similar_products for item in sublist]

    #split all elements in the list by .
    similar_products = [x.split(".") for x in similar_products]

    # flatten the list
    similar_products = [item for sublist in similar_products for item in sublist]

    # strip strings
    similar_products = [x.strip() for x in similar_products]

    # remove empty strings
    similar_products = list(filter(None, similar_products))




    # cumulative_list = []
    # for line in similar_products:
    #     # remove all empty elements
    #     line = list(filter(None, line))

    #     # remove all elements that are numbers
    #     line = [x for x in line if not x.isdigit()]

    #     # remove all elements that are less than 3 characters
    #     line = [x for x in line if len(x) > 3]

    #     # strip all elements of whitespace
    #     line = [x.strip() for x in line]

    #     # flatten the list
    #     line = [item for sublist in line for item in sublist]

    #     # append the line to the cumulative list
    #     if line:
    #         cumulative_list.append(line)



    
    print("Similar products: ", similar_products)

    # append the product names to the file
    with open("data-enhancer/similar-products.csv", "a") as f:
        for product in similar_products:
            f.write(str(item) + "," + str(product) + "\n")