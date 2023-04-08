import openai
import time

file_contents = ""

# read file similar-products.csv
with open('data-enhancer/ingridients.txt', 'r') as file:
    file_contents = file.read()

# split file contents into lines
lines = file_contents.split('\n')

# Set up OpenAI API credentials
# read value from a file and set it as the API key
with open("data-enhancer/chat-gpt.key", "r") as f:
    key = f.read()
    openai.api_key = key
# print(key, type(key))



# create an empty file to append the responses to
with open("data-enhancer/cleaned-ingridients.txt", "w") as f:
    pass



for line in lines:
    if(line.strip == ""):
        continue

    pair = line.split('>>')
    prod = pair[0] # get the product name
    print("###",prod)

    ingr = pair[1] # get the product ingredients
    if(len(ingr) > 30):
        with open("data-enhancer/cleaned-ingridients.txt", "a") as f:
            f.write(line + '\n')
        continue
    
    for attempt in range(3):

        # Define your prompt
        prompt = "List comma separated list of all ingredients of the product " + str(prod)

        # Send a request to OpenAI's API
        response = openai.Completion.create(
            engine="davinci-instruct-beta",
            prompt=prompt,
            temperature=0.75,
            max_tokens=1024,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0.6,
            stop=None
        )

        print(">RAW Response>", response.choices[0].text)


        separated = response.choices[0].text.split(',')

        # strip whitespace
        separated = [x.strip() for x in separated]

        # remove empty strings
        separated = list(filter(None, separated))

        # separate by new line
        separated = [x.split('\n') for x in separated]

        # flatten the list
        separated = [item for sublist in separated for item in sublist]

        if(len(','.join(separated)) > 30):
            break
        else:
            print("###",prod, "Attempt", attempt, "failed")
            time.sleep(1)

    # save to file
    with open("data-enhancer/ingridients.txt", "a") as f:
        f.write(prod + '>>' + ','.join(separated) + '\n')

    # wait for 1 second
    time.sleep(1)