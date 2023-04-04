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
    prompt = "for the product " + str(item) + ", list 10 food products which are similar to it and give all ingredients of each of them"

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

    # Print out the response from ChatGPT
    print(response.choices[0].text)

    # Add a delay to prevent hitting the API rate limit
    time.sleep(5)

    # Append the response to the file
    with open("data-enhancer/chat-gpt-responses.txt", "a") as f:
        f.write(response.choices[0].text)
