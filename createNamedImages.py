import pandas as pd
import os
import openai
import urllib.request

def file_exists(filename):
    return os.path.isfile(filename)

# Load your API key from an environment variable or secret management service
openai.api_key = os.getenv("OPENAI_API_KEY")

count = 1

listofobjects = pd.read_csv("data/unigram_freq.csv")
cleanlist = pd.DataFrame(listofobjects, columns=['count','word'])

print(listofobjects)
print(cleanlist)

for index, row in cleanlist.iterrows():
    # Extract the values of the 'column_name_1' and 'column_name_2' columns
    value_1 = row['count']
    value_2 = row['word']
    # Print the values

    filename = (f'{value_2}.png')
    if file_exists(filename):
        print(f'{filename} exists')
    else:
        print(f'{filename} does not exist and will be created')

        response = openai.Image.create(
        prompt=value_2,
        n=1,
        size="256x256"
        )

        image_url = response['data'][0]['url']
        file_name = f"{value_2}.png"
        count = count + 1

        urllib.request.urlretrieve(
        image_url,
        file_name)