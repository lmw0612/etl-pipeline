import json
import re

import pandas as pd

with open("recipes.json", "r") as f:
    data = f.read()
    data = data.rstrip()
    data = data.split("\n")

data = list(map(lambda x: json.loads(x), data))
df = pd.DataFrame(data)

name_list = ['chili', 'Chili', 'Chilies', 'chilies', 'chill', 'chiles', 'Chiles', 'Chill']
# filter chili in the ingredients
df = df[df['ingredients'].str.contains('|'.join(name_list))]


# parsing preptime & cooktime
def parse(word):
    word = re.sub("[^0-9H]", '', word)
    if word == '':
        return - 1

    words = word.split('H')
    if len(words) == 2:
        hour = int(words[0])
        if words[1] != '':
            minute = int(words[1])
        else:
            minute = 0
    else:
        hour = 0
        minute = int(words[0])

    return hour * 60 + minute


df['cookTime'] = df['cookTime'].apply(parse)
df['prepTime'] = df['prepTime'].apply(parse)

df['difficultyTime'] = df['cookTime'] + df['prepTime']

# for loop to define difficulty
difficulty = []
for row in df['difficultyTime']:
    if row > 60:
        difficulty.append('Hard')
    elif row >= 30 & row <= 60:
        difficulty.append('Medium')
    elif row > 0 & row <= 30:
        difficulty.append('Easy')
    else:
        difficulty.append('Unknown')

df['difficulty'] = difficulty

df.to_csv('etl.csv')
