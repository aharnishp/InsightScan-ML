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



# Define your list of items to ask ChatGPT about
items = ["Amul Butter"] #, "Cadbury Dairy Milk Silk - Bubbly", "Haldiram's Moong Dal", "Maggi 2-Minute Noodles - Masala"]

# Loop through each item in the list and ask ChatGPT
for item in items:
    # Define your prompt for ChatGPT
    # prompt = "list the ingredients of the 10 food products which are similar to " + str(item)
    # prompt = "for the product " + str(item) + ", list 10 food products which are similar to it and give all ingredients of each of them"
    
    prompt = "List 10 branded food products similar to the product " + str(item)  + " comma separated"


    # Call the OpenAI GPT-3 API to generate a response
    response = openai.Completion.create(
        # engine="gpt-3.5-turbo",
        engine="davinci-instruct-beta",
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.7,
    )

    # now for the response, we need to do some processing
    # sample output of above request:

        # - Cell Phone Cream

        # - Kroger's Salted Butter

        # - Kroger's Natural Butter

        # - Kroger's Sour Cream

        # - Kroger's Ricotta Cheese

        # - Kroger's Sour Cream

        # - Kroger's Sour Cream


    # Get the name of prooducts from the response

    print("Raw response: ", response.choices[0].text)

    # similar_products = response.choices[0].text.replace("-", "").split("\n")
    similar_products = response.choices[0].text.split(",")

    # remove space in front and back
    similar_products = [x.strip() for x in similar_products]

    # drop empty string
    similar_products = [x for x in similar_products if x]

    # drop the first element, as it is the prompt itself
    similar_products = similar_products[1:]
    
    print("Similar products: ", similar_products)

    # drop the first element, as it is the prompt itself
    similar_products = similar_products[1:]

    for similar_product in similar_products:
        # Define your prompt for ChatGPT
        prompt = "List all ingredients of the " + str(similar_product) + " comma separated"

        # Call the OpenAI GPT-3 API to generate a response
        response = openai.Completion.create(
            # engine="gpt-3.5-turbo",
            engine="davinci-instruct-beta",
            prompt=prompt,
            max_tokens=100,
            n=1,
            stop=None,
            temperature=0.7,
        )

        print("Raw ing response for " + similar_product + ": ", response.choices[0].text)

        ingredients = response.choices[0].text.replace("-", "").split("\n")


        # drop empty string
        ingredients = [x for x in ingredients if x]

        # drop the first element, as it is the prompt itself
        ingredients = ingredients[1:]

        print(similar_product)
        print(ingredients)

        # now we have the ingredients list, we need to write it to a file
        with open("data-enhancer/chat-gpt-responses.txt", "a") as f:
            # write name of product itself
            # f.write(str(similar_prosuct) + "\n")
            f.write(str(similar_product) + "\t" + str(ingredients) + "\n")

        time.sleep(3)


    # Print out the response from ChatGPT
    print(response.choices[0].text)

    # Add a delay to prevent hitting the API rate limit
    time.sleep(1)

    # Append the response to the file
    # with open("data-enhancer/chat-gpt-responses.txt", "a") as f:
        # f.write(response.choices[0].text)
