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

items = ["Amul Butter", "Cadbury Dairy Milk Silk - Bubbly", "Haldiram's Moong Dal", "Maggi 2-Minute Noodles - Masala"]

# Loop through each item in the list and ask ChatGPT
for item in items:
    # Define your prompt for ChatGPT
    # prompt = "list the ingredients of the 10 food products which are similar to " + str(item)
    # prompt = "for the product " + str(item) + ", list 10 food products which are similar to it and give all ingredients of each of them"
    
    # prompt = "get 10 food product brand names similar to the product " + str(item)  + " comma separated"
    # prompt = "list the name of the 10 food products which are similar to " + str(item) + " comma separated"
    # prompt = "Get comma separated list of 10 products like " + str(item)
    # prompt = "Get comma separated list of 10 products like " + str(item)

    # prompt = "Generate a list of branded food products that are similar to " + str(item) + ". Please include the product name, brand, and any relevant details such as flavor or packaging. Use your knowledge of the food industry and consumer preferences to generate the most relevant and up-to-date recommendations. "
    # prompt = "Generate a list of branded food products that are similar to the following product: " + str(item) + ". Please provide the product name in the format 'Brand, Product Name', with a comma separating the brand and product name. Please include the product name, brand, and any relevant details such as flavor or packaging. Use your knowledge of the food industry and consumer preferences to generate the most relevant and up-to-date recommendations. "
    prompt = "Generate a comma-separated list of branded food products that are similar to " + str(item) + ". Include only the product name and brand, with no additional words or descriptions. Please use your knowledge of the food industry and consumer preferences to generate the most relevant and up-to-date recommendations."


    print("prompt: ", prompt)

    # Call the OpenAI GPT-3 API to generate a response
    response = openai.Completion.create(
        # engine="gpt-3.5-turbo",
        engine="davinci-instruct-beta",
        # engine="ada-instruct-beta",
        prompt=prompt,
        max_tokens=200,
        n=1,
        stop=None,
        temperature=0.75,
    )


    print("Raw response: ", response.choices[0].text)

    # similar_products = response.choices[0].text.replace("-", "").split("\n")
    similar_products = response.choices[0].text.split(",")

    # remove bullet points
    similar_products = [x.replace("-", "") for x in similar_products]

    # remove all numbered bullet points
    


    # drop only numeric elements in the list
    similar_products = [x for x in similar_products if not x.isdigit()]

    # remove space in front and back
    similar_products = [x.strip() for x in similar_products]

    # drop empty string
    similar_products = [x for x in similar_products if x]

    # drop the first element, as it is the prompt itself
    similar_products = similar_products[1:]
    
    print("Similar products: ", similar_products)

    # drop the first element, as it is the prompt itself
    similar_products = similar_products[1:]

    # append the product names to the file
    with open("data-enhancer/similar-products.csv", "a") as f:
        for product in similar_products:
            f.write(item + "," + product + "\n")